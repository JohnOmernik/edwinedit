# edwinedit
A GUI Json Editor for Edwin Matrix based on Flask



----
This editer is based on https://github.com/icchan/json-tinker code and runs in flask, it's pretty much a generic json editor with an "add" field that adds a whole child item for Edwin

It also loads, archives (to app_root/archive) and saves the changes you make


To use, map this directory to /app/code in the built container. 

Map your edwin_org directory to /app/edwin_org (or use the ENV variable APP_ROOT)

Todo:
- Valdiator
- Better Archiving/saving
- Better control of UI
- Loading different Edwin.jsons
- Snarkyness



