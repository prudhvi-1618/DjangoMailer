from django.core.management.base import BaseCommand
from api.models import Campaign, Subscriber
from django.utils.timezone import now
from api.tasks import send_campaign_email



class Command(BaseCommand):
    help = 'Dispatching campaign emails'

    def handle(self, *args, **options):
        today = now().date()
        campaign = Campaign.objects.filter(published_date__date=today).first()
        if not campaign:
            self.stdout.write("No campaign to send today.")
            return

        campaign_data = {
            'subject': campaign.subject,
            'preview_text': campaign.preview_text,
            'html_content': campaign.html_content,
            'plain_text_content': campaign.plain_text_content,
            'article_url': campaign.article_url,
        }

        subscribers = Subscriber.objects.filter(is_active=True)
        for sub in subscribers:
            send_campaign_email.delay(sub.email, sub.name, campaign_data)

        self.stdout.write(self.style.SUCCESS("Campaign dispatch enqueued for all subscribers."))
