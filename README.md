# 🎉 MyFest

Self-hosted Event & Shift Management System for Raspberry Pi, Vereine und Festivals.

MyFest hilft bei der Organisation von Teams, Helfern und Schichten – inklusive Warteliste, Rollenverwaltung, Kalenderexport und später QR-Check-in.

---

## ✨ Features

### 👤 Benutzer & Rollen

* Selbstregistrierung
* Benutzer durch Admin anlegen
* Rollen:

  * Admin
  * Teamleiter
  * Helfer

### 🧑‍🤝‍🧑 Teams

* Teams erstellen
* Helfer Teams zuweisen
* Teamleiter verwalten

### 🕒 Schichtplanung

* Schichten erstellen
* Maximale Teilnehmerzahl
* Automatische Zuweisung
* Warteliste bei voller Schicht

### 📅 Kalender

* Dienstplan
* ICS Export
* Outlook / Google / Apple Kalender kompatibel

### 📲 Eventfunktionen (spätere Version)

* QR Check-in
* Erinnerungen
* Telegram Benachrichtigungen
* Dashboard

---

## 📸 Screenshots

### Dashboard

![Dashboard](docs/screenshots/dashboard.png)

### Kalender

![Kalender](docs/screenshots/calendar.png)

### Schichtübersicht

![Shifts](docs/screenshots/shifts.png)

---

## 🐳 Installation (Docker)

### Voraussetzungen

* Raspberry Pi 4 (empfohlen 4–8 GB RAM)
* Docker
* Docker Compose
* Git

---

### Repository klonen

```bash
git clone https://github.com/D4N154NN5/MyFest.git

cd myfest
```

---

### Umgebungsdatei anlegen

```bash
cp .env.example .env
nano .env   # SECRET_KEY und Passwörter anpassen
```

---

### Container starten

```bash
docker compose up --build -d
```

---

### Datenbankmigrationen

```bash
docker compose exec web python manage.py migrate
```

---

### Admin Benutzer erstellen

```bash
docker compose exec web python manage.py createsuperuser
```

---

### Anwendung öffnen

Browser:

```text
http://localhost:8000
```

oder im Netzwerk:

```text
http://<RASPBERRY_PI_IP>:8000
```

---

## 🏗 Projektstruktur

```text
myfest/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── .gitignore
├── requirements.txt
├── manage.py
├── myfest/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── apps/
    ├── accounts/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── models.py
    │   ├── forms.py
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/
    │       └── accounts/
    │           ├── login.html
    │           ├── register.html
    │           └── dashboard.html
    └── events/
        ├── __init__.py
        ├── admin.py
        ├── models.py
        ├── views.py
        ├── urls.py
        └── templates/
            └── events/
                ├── event_list.html
                ├── event_detail.html
                ├── shift_list.html
                └── shift_detail.html

```

---

## 🔧 Technologie

Backend:

* Django
* Django REST Framework
* PostgreSQL

Frontend:

* HTML
* Bootstrap
* FullCalendar (geplant)

Services:

* Redis
* Celery
* Docker

---

## 🚀 Roadmap

### Version 1

* [x] Benutzerverwaltung
* [x] Teams
* [x] Schichten
* [x] Warteliste

### Version 2

* [ ] FullCalendar
* [ ] QR Check-in
* [ ] Kalenderexport

### Version 3

* [ ] Telegram Integration
* [ ] E-Mail Erinnerungen
* [ ] Push Benachrichtigungen
* [ ] Mobile PWA

---

## 📄 Lizenz

MIT License

---

Made with ❤️ using Django + Raspberry Pi
