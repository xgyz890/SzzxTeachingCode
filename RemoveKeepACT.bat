@echo off
md "d:\desktop\act"
xcopy e:\ACT��� d:\desktop\act /s/y
echo ����ɾ���ļ������Ե�......
del /f /s /q e:\
rd /q /s e:\
echo ɾ�����
md "e:\ACT���"
xcopy d:\desktop\act e:\ACT��� /s/y
del /f /s /q d:\desktop\act
rd /q /s d:\desktop\act
del d:\desktop\remove-e-keep-act.bat