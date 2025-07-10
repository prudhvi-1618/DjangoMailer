

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/prudhvi-1618/DjangoMailer/.git
cd DjangoMailer
```

### 2. Set Up Virtual Environment

```bash
python -m venv env

# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root of the project with the following content:

```env
EMAIL_HOST=smtp.mailgun.org
EMAIL_PORT=587
EMAIL_HOST_USER=your_mailgun_user
EMAIL_HOST_PASSWORD=your_mailgun_password
EMAIL_USE_TLS=True
EMAIL_FROM=noreply@example.com

CELERY_BROKER_URL=redis://localhost:6379/0
SECRET_KEY=your_secret_key
DEBUG=True
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Start the Django Server

```bash
python manage.py runserver
```

### 8. Run Redis (via Docker)

```bash
docker run -d --name redis -p 6379:6379 redis
```

### 9. Start Celery Worker (Windows compatible)

```bash
celery -A backend worker --loglevel=info --pool=solo
```

### 10. Send Campaign Emails (for today's campaigns)

```bash
python manage.py send_mail
```
