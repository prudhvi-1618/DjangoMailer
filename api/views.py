from django.shortcuts import render
from .models import Subscriber


def Unsubscribe_user(request):

    email = request.GET.get('email', '').strip()

    if not email:
        return render(request, 'unsubscribe.html', {
            'success': False,
            'message': 'No email provided.'
        })

    try:
        subscriber = Subscriber.objects.get(email=email)
        if subscriber.is_active == False:
            return render(request, 'unsubscribe.html', {
                'success':False,
                'message':'This email is already in our unsubscription list. No need to unsubscribe',
                'mail_id':email
            })
        subscriber.is_active = False
        subscriber.save()
        return render(request, 'unsubscribe.html', {
            'success':True,
            'mail_id':email
        })
    except Subscriber.DoesNotExist:
        return render(request, 'unsubscribe.html', {
            'success':False,
            'message':'This email is not in our subscription list.',
        })


def resubscribe(request):
    email = request.GET.get('email', '').strip()

    if not email:
        return render(request, 'resubscribe_result.html', {
            'success': False,
            'message': 'No email provided.'
        })

    try:
        subscriber = Subscriber.objects.get(email=email)
        if subscriber.is_active:
            return render(request, 'resubscribe.html', {
                'success': False,
                'message': 'You are already subscribed.',
            })

        subscriber.is_active = True
        subscriber.save()
        return render(request, 'resubscribe.html', {
            'success': True,
        })
    except Subscriber.DoesNotExist:
        return render(request, 'resubscribe.html', {
            'success': False,
            'message': 'Email not found in our records.',
        })
