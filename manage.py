# # #!/usr/bin/env python
# # """Django's command-line utility for administrative tasks."""
# # import os
# # import sys


# # def main():
# #     """Run administrative tasks."""
# #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plum_tiger_backend.settings")
# #     try:
# #         from django.core.management import execute_from_command_line
# #     except ImportError as exc:
# #         raise ImportError(
# #             "Couldn't import Django. Are you sure it's installed and "
# #             "available on your PYTHONPATH environment variable? Did you "
# #             "forget to activate a virtual environment?"
# #         ) from exc
# #     execute_from_command_line(sys.argv)


# # if __name__ == "__main__":
# #     main()
# # # #!/usr/bin/env python
# # # """Django's command-line utility for administrative tasks."""
# # # import os
# # # import sys


# # # def main():
# # #     """Run administrative tasks."""
# # #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
# # #     try:
# # #         from django.core.management import execute_from_command_line
# # #     except ImportError as exc:
# # #         raise ImportError(
# # #             "Couldn't import Django. Are you sure it's installed and "
# # #             "available on your PYTHONPATH environment variable? Did you "
# # #             "forget to activate a virtual environment?"
# # #         ) from exc
# # #     execute_from_command_line(sys.argv)


# # # if __name__ == '__main__':
# # #     main()

# # #!/usr/bin/env python
# # """Django's command-line utility for administrative tasks."""
# # import os
# # import sys


# # def main():
# #     """Run administrative tasks."""
# #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
# #     try:
# #         from django.core.management import execute_from_command_line
# #     except ImportError as exc:
# #         raise ImportError(
# #             "Couldn't import Django. Are you sure it's installed and "
# #             "available on your PYTHONPATH environment variable? Did you "
# #             "forget to activate a virtual environment?"
# #         ) from exc

# #     # 👇 Modify this block to inject default IP if no args are provided
# #     if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == "runserver"):
# #         sys.argv = [sys.argv[0], "runserver", "192.168.0.106:8000"]

# #     execute_from_command_line(sys.argv)


# # if __name__ == '__main__':
# #     main()

# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plum_tiger_backend.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc

#     # Auto-start on specific IP if no args or only 'runserver' is passed
#     if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == "runserver"):
#         sys.argv = [sys.argv[0], "runserver", "192.168.0.106:8000"]

#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plum_tiger_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Automatically bind to all IPs if no args or only 'runserver' is passed
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == "runserver"):
        sys.argv = [sys.argv[0], "runserver", "0.0.0.0:8000"]

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
