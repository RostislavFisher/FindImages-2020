### Поиск скрытых фотографий в сети
Для запуска скрипта потребуются следующие библиотеки:
- beautifulsoup4 (bs4)
- requests

### Последовательность установки софта:
- Создайте виртуальное окружение (необязательный шаг)

      virtualenv myNameOfEnv

- Зайдите в виртуальное окружение:


Windows:

      source myNameOfEnv\Scripts\activate.bat
      

Unix:

    source myNameOfEnv\bin\activate

-Скачивание библиотек:

    pip install beautifulsoup4
    pip install requests
      
Запуск скрипта :

    python main.py 
    
Автоматически начнется бесконечный поиск картинок из хостинга imgur.

Для поиска из других хостинг-сайтов, нужно написать комманду:

    python main.py --siteToPars 2
   
В этом примере мы даем команду скрипту на парсинг хостинга под номером 2(LightShot).

Также, можно применить ограничение на количество получаемых картинок:

    python main.py --amountOfIterations 54
    
В случае этой команды, скрипт скачает 54 изображения и сохранит их.


Можно задать расширение файла, которое мы будем получать(по умолчанию - .png):

    python main.py --fileExpansion .jpg
