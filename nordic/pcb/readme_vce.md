SanskarBiswalToday at 6:11 PM
# Loading Symbol Libraries

Some Symbol Libraries, if not present in the User System will not load and instead appear as a Question Mark in a Square Box

The VCE provides these libraries in the User_Libs Folder.

## Steps to Load New Symbol in KiCAD

1. Open Schematic File. (.kicad_sch)
2. Goto Tools -> Symbol Library Editor (This Should Open in a New Window)
3. In Library Editor goto File -> Add Library...
4. Select the corresponding library from User_Libs Folder. The name will be the same as the Symbol. Go into the folder and select the file with .lib extension. This will add the lib to the symbol.
eg: If missing symbol is NRF52, goto the MSF50SFA_NRF52/MSF50SFA_VCE.lib is the library you need to add.
5. Return to Schematic and place Cursor on the Missing Symbol.
6. Press E
7. In the Symbol Panel There is Library Selection Textbox
8. Click the Browse.. button next to it.
9. Search for the correct Library and double-click to select.
10. The correct symbol should be loaded.