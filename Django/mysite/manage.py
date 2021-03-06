#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    try:
        from django.core.management import execute_from_command_line
        import django

        django.setup()
        from floybd.models import Setting
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    if len(sys.argv) == 5:
        galaxyIp = sys.argv.pop(4)
        print("Liquid Galaxy IP is : " + str(galaxyIp))
        lgIp, created = Setting.objects.get_or_create(key="lgIp")
        lgIp.value = galaxyIp
        lgIp.save()
        command = "ssh-keyscan -H "+str(galaxyIp)+" >> ~/.ssh/known_hosts"
        os.system(command)

    execute_from_command_line(sys.argv)
