from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ExpenseReport
from .serializers import ExpenseReportSerializer

class ExpenseFormSubmissionView(APIView):
    def get(self, request):
        forms = ExpenseReport.objects.all()
        serializer = ExpenseReportSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Validation errors: ", serializer.errors)
        print("Request data: ", request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateStatusView(APIView):
    def post(self, request, pk):
        try:
            form = ExpenseReport.objects.get(pk=pk)
            action = request.data.get('status')
            if action in ['Approved', 'Denied', 'Pending']:
                form.status = action
                form.save()
                return Response({'message': 'Status updated successfully'}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
        except ExpenseReport.DoesNotExist:
            return Response({'error': 'Form not found'}, status=status.HTTP_404_NOT_FOUND)
