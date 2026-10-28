[app]
title = Poiotita
package.name = poiotita
package.domain = gr.poiotita
source.dir = .
source.include_exts = py
source.exclude_dirs = .github, bin, .buildozer
version = 1.5
requirements = python3,kivy==2.3.1,certifi,android,libzbar,pyzbar
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, CAMERA, VIBRATE
android.api = 34
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 0
