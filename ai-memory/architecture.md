# Архитектура `src/guide.html`

Один файл ~3300 строк: CSS-токены и стили, разметка вкладок, затем один `<script>` (IIFE). Сборка `tools/build_site.py` оборачивает его в `index.html` (+ manifest, иконки) и пишет `sw.js` с версией по хэшу содержимого.

## Вкладки и маршрутизация
- Вкладки (`nav.tabs`): Старт, Уроки, Панель, Рецепты, Задания, Справка.
- `views` = start, panel, lessons, skills, tracks, recipes, challenges, cheats, menus, about, videos; плюс `v-branch` (страница раздела).
- `route()` читает hash: `#branch-<id>`, `#l-<n>[-s<N>|-full]` (глубокие ссылки, `openDeep()` раскрывает урок/шаг и в режиме по шагам ставит фокус на шаг), иначе имя view.
- Подменю `.subnav`: «Путь/Навыки/Собери трек» в уроках и «Шпаргалка/Меню/О приборе/Видео» в справке.

## Данные уроков
`lessons=[{n, lv, t, time, page, goal, steps[], check, task, warn, src, tc[], gloss, chords, ...}]`, плюс `GENRE_LESSONS` (push в lessons).
Дополнительные поля урока:
- `ear:["hat",…]` — упражнения «На слух» из `EARS`.
- `diag:["silent"]` — тренажёр поиска причины (`DIAGS`).
- `drill` (объект или массив) — упражнение: `{t, goal, steps[], table?, tally?, clips?, check}`.
- `table` — таблица под шагами; `more[]` — «Дополнительные опыты»; `fixes[]` — «Как исправить ошибку»; `full[]` — «Если все пэды заняты».
- `ext:[[label,url,"roland"|"com"|"idea"]]` — блок «Не из руководства».
- `verify:{q, back, backLabel}` — экран «Проверь на приборе» перед завершением в режиме по шагам.
- `stage` / `stages[]` — блоки сквозного трека или сравнения (см. ниже).
- `SECTIONS` — разделы (`genre:1`, `bpm`, `dur`, `recipe`); `PREFIX` — буквы меток; `PARTS` — деление на занятия по индексу шага; `SES`, `GL`, `LESSON_LINKS`, `TIPS`.

## Сетки и звук
- `GRIDS[n]` — сетки урока; `gridHTML(g,id)`: строки `{n,pad,k,s[],v{},p{},sub{},t{} (микросдвиг),lvl,bars (tone/pad),mg (mute group),echo{t,fb,n,on},pm{} (питч metal),lp,lpS{}}`, `len` (16/32/64, страницы по 16), `scale` (`1_16`,`8t`…), `swing`, `hl[]`+`hlr`, `noplay`, `note`. Многотактовые tone-партии: кнопки «Такт k», в игре показывается звучащий такт.
- `playSeq(id)` — планировщик WebAudio; A/B-переключение на границе такта через `seqNext`, смена темпа при свопе.
- Голоса `hit(k)`: kick, snare, clap, hat, ohat, metal, amb, crackle, rustle, click, zip; `tone()`/`bassNote()`; `dest()` даёт lowpass по `CUR_LP`.
- `useGrid(id,src)` — состояние сетки с сохранением правок в localStorage (`p6grid`), кнопка «Вернуть пример».

## Блоки
- **EARS** (`earHTML`) — A/B «На слух»: вопрос, варианты/выбор шага, «Показать шаги», «Повтори на P-6» (показывается после верного ответа), «Другое задание».
- **TRACK** (`trkHTML`) — «Сквозной трек»/«Сравнение»: варианты `V:[{lbl,rows,len,hl,…}]` или `A/B`, кнопки по вариантам, сетка выбранного/звучащего варианта; `overview`, `final`, `start` (карточка «Начать с этого урока», `trkStart`, `startRows`, `startCell`), `sim`, `first`, `also`, `track:"cmp"`.
- `regStages()` переносит `stage/stages` уроков в `TRACK`.
- DIAGS, TALLY (журнал «+/−»), clipsHTML (схема клипов Ableton).

## Хранилище (localStorage)
`p6done` (отметки `"<n>-<stepIndex>"`), `p6open`, `p6focus`, `p6last`, `p6chd`, `p6chf`, `p6undo`, `p6grid`, `p6mig06b` (разовый перенос отметок урока 06, только если есть индексы ≥8).

## Подписи шагов
`stepNames()` внутри `fmt()` дописывает к «шаг/шаги N» подпись кнопки: `STEPK` = C, C♯ … B, C, OCT−, OCT+, TIE (шаг 17+ — та же кнопка на следующей странице). Не трогает «шаг N (…)» и «шаг N из». Минимальный размер подписи 12px.

## Ловушки
- Не использовать `const` до объявления (TDZ): `R`, `RX`, `EARS` — порядок объявлений важен (`BLIND_EAR` присваивается после `EARS`).
- `relabel()` меняет только «урок NN» по id; статический HTML не проходит через него.
- Отметки привязаны к индексу шага — при перестановке шагов старые отметки съезжают.
