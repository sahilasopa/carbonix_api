import json
import secrets
from datetime import datetime

import OTPLessAuthSDK
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CarboUser, StationProfile, Journey
from math import cos, asin, sqrt, pi

from authentication.serializers import StationProfileSerializer, JourneySerializer

otpless_client_id = ""
otpless_client_secret = ""


# read previous trips via id
# cru wishlist, (Create: product id), Update(add balance,  add item)
# wishlist 3rd model
# get user
# transaction from user to user, amount date time, create read
class AddTripsAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        id = data.get("user_id")
        trips = Journey.objects.filter(user_id=id, in_progress=False)
        data = JourneySerializer(trips, many=True).data
        return Response({"data": data})


class ProfileAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user_id = data.get("id")
        name = data.get("name")
        dob = data.get("dob")
        user = CarboUser.objects.get(pk=user_id)
        user.name = name
        user.dob = dob
        user.save()
        return Response("OK")


class StartJourneyAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user_id = data.get("user_id")
        type = data.get("type")
        start_station_id = data.get("start_station_id")
        journey = Journey.objects.create(
            user_id=user_id,
            type=type,
            start_stop=StationProfile.objects.get(id=start_station_id),
            in_progress=True,
            start_time=datetime.now(),
        )
        return Response({"id": journey.id})


class StationProfileAPIView(APIView):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        stations = StationProfile.objects.all()
        serializer = StationProfileSerializer(stations, many=True)
        return Response({"data": serializer.data})


class EstimatedDistanceAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        start_station = StationProfile.objects.get(id=data.get("start_id"))
        end_station = StationProfile.objects.get(id=data.get("end_id"))
        temp = Journey.objects.create(
            user=None,
            type="Train",
            start_stop=start_station,
            end_stop=end_station,
            start_time=datetime.now()
        )
        credits = temp.get_credits()
        temp.delete()
        return Response({"data": credits})


class EndJourneyAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        journey_id = data.get("trip_id")
        end_station_id = data.get("station_id")
        journey = Journey.objects.get(
            id=journey_id
        )
        journey.end_stop = StationProfile.objects.get(id=end_station_id)
        journey.in_progress = False
        journey.end_time = datetime.now()
        journey.save()
        return Response({"credits": journey.get_credits(),
                         "carbon_saved": journey.calculate_carbon_emissions_saved(),
                         "time_taken": journey.calculate_time_taken(),
                         "start_name": journey.start_stop.name,
                         "end_name": journey.end_stop.name
                         })


class SendOtpAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        phone_number = data.get("phoneNumber")
        try:
            otp_details = OTPLessAuthSDK.OTP.send_otp(
                phone_number,
                None,
                "SMS",
                None,
                None,
                "300",
                4,
                otpless_client_id,
                otpless_client_secret
            )
            return Response(otp_details, status=200)
        except Exception as e:
            print(f"An error occurred: {e}")
            return Response({"message": "Error Occurred"}, status=400)


class VerifyOtpAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        phone_number = data.get("phoneNumber")
        try:
            otp_details = OTPLessAuthSDK.OTP.veriy_otp(
                data.get("orderId"),
                data.get("otp"),
                None,
                phone_number,
                otpless_client_id,
                otpless_client_secret
            )
            if otp_details.get('isOTPVerified'):
                uid = ''.join(
                    secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(28)
                )
                user = CarboUser.objects.filter(phone_number=phone_number).first()
                if user is not None:
                    return Response({"uid": user.id}, status=200)
                else:
                    CarboUser.objects.create(
                        id=uid,
                        name=data.get("name"),
                        phone_number=phone_number,
                    )
                return Response({
                    "isVerified": True,
                    "uid": uid,
                }, status=200)
            else:
                return Response({
                    "isVerified": False,
                    "message": "Invalid OTP"
                }, status=401)
        except Exception as e:
            print(f"An error occurred: {e}")
            return Response({"message": "Error Occurred"}, status=400)


class ResendOtpAPIView(APIView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            otp_details = OTPLessAuthSDK.OTP.resend_otp(
                data.get("order_id"),
                otpless_client_id,
                otpless_client_secret
            )
            return Response(status=200)
        except Exception as e:
            print(f"An error occurred: {e}")
            return Response({"message": "Please try later"}, status=400)
