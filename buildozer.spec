#buildozer --profile demo android debug

[app]
title = Bomb Defusal
package.name = bombdefusal
package.domain = org.ricdefuse.logicgame
version = 1.0
source.include_exts = py,kv
source.dir = .


bootstrap = sdl2


android.javac = /usr/lib/jvm/java-21-openjdk-*/bin/javac
log_level = 2

requirements = python3,kivy,cython,pyjnius@git+https://github.com/kivy/pyjnius.git@master#egg=pyjnius
p4a.branch = develop



# Optional: if using pyjnius, plyer, etc., list them too

[buildozer]
log_level = 2

