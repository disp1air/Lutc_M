В двух словах, модули обеспечивают простой способ организации компонентов в систему автономных пакетов переменных, известных как пространства имен. Все имена, определяемые на верхнем уровне модуля, становятся атрибутами объекта импортируемого модуля. Операция импорта предоставляет доступ к именам в глобальной области видимости модуля. Таким образом, в процессе импортирования глобальная область видимости модуля образует пространство имен атрибутов объекта модуля.
В конечном счете модули позволяют связывать отдельные файлы в крупные программные системы.

модуль a может импортировать модуль b, который импортирует модуль c, который в свою очередь может еще раз импортировать модуль b, и так далее.

Интерпретатор Python поставляется с обширной коллекцией дополнительных модулей, которая известна как стандартная библиотека. Эта коллекция насчитывает порядка 200 крупных модулей и содержит платформонезависимую поддержку распространенных задач программирования: интерфейсы операционных систем, организацию хранилищ объектов, поиск по шаблону, сетевые взаимодействия, создание графического интерфейса и многих других. Ни один из этих инструментов не является непосредственной частью языка Python, но вы можете использовать их, импортируя соответствующие модули.  

**Как работает импорт:**  
Это самые настоящие операции времени выполнения, которые выполняют следующие действия, когда программа впервые импортирует заданный файл:  
 - отыскивают файл модуля
 - компилируют в байт-код(если необходимо)
 - Запускают программный код модуля, чтобы создать объекты, которые он определяет

все три действия выполняются, только когда модуль впервые импортируется во время выполнения программы, – все последующие операции импорта того же модуля пропускают эти действия и просто выбирают уже находящийся в памяти объект модуля. Технически это обеспечивается за счет того, что интерпретатор сохраняет информацию о загруженных модулях в словаре с именем sys.modules и проверяет его при выполнении каждой операции импортирования. Если модуль отсутствует в словаре, выполняется трехэтапный процесс, описанный выше.

**1. Поиск**  
Прежде всего, интерпретатор должен определить местонахождение файла модуля, указанного в инструкции import.  

**2. Компиляция**  
После того как в пути поиска модулей будет найден файл, соответствующий имени в инструкции import, интерпретатор компилирует его в байт-код, если это необходимо. Интерпретатор проверяет время создания файла и пропускает этап компиляции исходного программного кода, если файл с байт-кодом .pyc не старше, чем соответствующий ему файл .py с исходным текстом. 

Кроме того, если Python обнаружит в пути поиска только файл с байт-кодом и не найдет файл с исходным текстом, он просто загрузит байт-код (это означает, что вы можете распространять свою программу исключительно в виде файлов с байт-кодом и не
передавать файлы с исходными текстами). Другими словами, этап компиляции пропускается, если можно ускорить запуск программы. Если вы измените исходный программный код, Python автоматически скомпилирует байт-код при следующем запуске программы.  

Обратите внимание, что компиляция выполняется в момент импортирования файла. По этой причине файл .pyc с байт-кодом для главного файла программы обычно не создается, если только он не был импортирован еще куда-нибудь – файлы .pyc создаются только при импортировании файлов. Байт-код главного файла программы создается в памяти компьютера, а байт-код импортированных файлов сохраняется в файлах для ускорения будущих операций импорта.  

**3. Запуск**  
На последнем шаге операции импортирования производится запуск байт-кода модуля. Все инструкции в файле модуля выполняются по порядку, сверху вниз, и любые операции присваивания, которые встретятся на этом шаге, будут создавать атрибуты конечного объекта модуля. Таким образом, этот этап выполнения создает все инструменты, которые определяются модулем.

На этом последнем шаге операции импортирования фактически запускается программный код модуля, поэтому если программный код верхнего уровня в файле модуля выполняет какие-нибудь действия, результаты этих действий можно будет наблюдать во время импорта.  

Как видите, во время импорта выполняется достаточно много работы – производится поиск файла, в случае необходимости запускается компилятор и производится запуск программного кода. Вследствие этого любой заданный модуль по умолчанию импортируется только один раз за все время работы программы. При повторных попытках импортировать модуль все три шага просто
пропускаются, и повторно используется модуль, уже загруженный в память. Если вам потребуется еще раз импортировать файл, который уже был загружен, воспользуйтесь функцией imp.reload.  

Путь поиска модулей
