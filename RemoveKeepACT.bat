@echo off
md "d:\desktop\act"
xcopy e:\ACT软件 d:\desktop\act /s/y
echo 正在删除文件，请稍等......
del /f /s /q e:\
rd /q /s e:\
echo 删除完成
md "e:\ACT软件"
xcopy d:\desktop\act e:\ACT软件 /s/y
del /f /s /q d:\desktop\act
rd /q /s d:\desktop\act
del d:\desktop\remove-e-keep-act.bat