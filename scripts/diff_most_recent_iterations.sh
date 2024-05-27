$VISUAL -d $(ls -Art | grep .py | tail -n 2 | head -n 1) $(ls -Art | grep .py | tail -n 1)
