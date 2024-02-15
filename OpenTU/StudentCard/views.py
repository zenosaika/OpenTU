from django.shortcuts import render
from User.models import Student

import qrcode
import base64
from io import BytesIO

def gen_qrcode_by(id):
    qr_img = qrcode.make(id, box_size=15).get_image()
    data = BytesIO()
    qr_img.save(data, format='JPEG')
    data64 = base64.b64encode(data.getvalue()).decode('utf-8')
    return data64

def idcard_request(request):
    student = Student.objects.filter(user=request.user)
    context = {}
    if student:
        context['student'] = student[0]
        context['qrcode'] = gen_qrcode_by(student[0].student_id)
    else:
        # create new Student object for this user
        # go to new Student form
        ...
    return render(request, 'StudentCard/idcard.html', context)