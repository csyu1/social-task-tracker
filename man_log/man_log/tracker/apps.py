from django.apps import AppConfig


class TrackerConfig(AppConfig):
    name = 'man_log.tracker'
    verbose_name = "Trackers"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
