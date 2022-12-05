"""Configuration file for the app."""

from django.apps import AppConfig


class ReportConfig(AppConfig):
    """Various configuration settings."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'report'
