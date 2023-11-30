#!/usr/bin/env python
# モジュールをimport
import os
import sys

if __name__ == "__main__":
    # Djangoアプリケーションの設定を指定
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")
    # 例外処理
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Djangoの管理コマンドを実行
    execute_from_command_line(sys.argv)
