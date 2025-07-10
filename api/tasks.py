from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template import Template, Context
import os

# Raw HTML Email Template
base_mail_template = '''
<html>
<body style="margin:0; padding:0; background-color:#121212; color:#eeeeee; font-family: Arial, sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#121212; padding:20px 10px;">
    <tr>
      <td align="center">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background:#1e1e1e; border-radius:6px; padding:20px;">
          <tr>
            <td align="center" style="font-size:14px; color:#bbbbbb; padding-bottom:20px;">{{ preview_text }}</td>
          </tr>
          <tr>
            <td style="font-size:16px; line-height:1.5; padding-bottom:20px;">
              <p style="font-size:16px; margin-bottom:0px;">Hi, {{ name }}</p>
              {{ html_content|safe }}
            </td>
          </tr>
          <tr>
            <td align="center" style="padding-bottom:30px;">
              <p style="font-size:16px;">Click below to read the full article:</p>
              <a href="{{ article_url }}" style="display:inline-block; background:#bb86fc; color:#121212; text-decoration:none; padding:12px 24px; border-radius:4px; font-weight:bold; font-size:16px;">Read More</a>
            </td>
          </tr>
          <tr>
            <td style="font-size:12px; color:#777777; text-align:center; border-top:1px solid #333333; padding-top:20px;">
              If you no longer wish to receive these emails, <a href="{{ unsubscribe_url }}" style="color:#bb86fc;">Unsubscribe</a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
'''

@shared_task
def send_campaign_email(subscriber_email, name, campaign_data):
    context = Context({
        'name': name,
        'preview_text': campaign_data['preview_text'],
        'html_content': campaign_data['html_content'],
        'article_url': campaign_data['article_url'],
        'unsubscribe_url': f"http://127.0.0.1:8000/unsubscribe/?email={subscriber_email}",
    })

    template = Template(base_mail_template)
    html_rendered = template.render(context)

    msg = EmailMultiAlternatives(
        subject=campaign_data['subject'],
        body=campaign_data['plain_text_content'],
        from_email=os.getenv('EMAIL_FROM', 'noreply@example.com'),
        to=[subscriber_email],
    )
    msg.attach_alternative(html_rendered, "text/html")
    msg.send()