"""Тексты юридических страниц Hushwake на шести языках.

Английский — источник, остальные пять переведены с него. Обращение
неформальное во всех языках, как и в самом приложении: страницы написаны
голосом продукта, а не канцелярией. **Это решение стоит подтвердить
у юриста** — в договорных текстах чаще принято формальное «вы».

Правится этот файл, дальше `python3 build.py`. HTML не трогать.

ГЛАВНОЕ ПРАВИЛО: текст обязан совпадать с тем, что делает код. Сейчас
страницы утверждают, что приложение не ходит в сеть вовсе, хранит только
настройки и историю подъёмов, не трогает микрофон и датчики движения,
и что единственное системное разрешение — локальные уведомления (страховка
на случай свёрнутого приложения). Появится сеть, аналитика, аккаунты,
трекинг сна или что угодно ещё — эти страницы правятся в тот же заход,
на всех шести языках.

Отдельно: `terms` обязаны прямым текстом называть главное ограничение —
волна играет только с открытым приложением. Узнать это из условий после
того, как проспал, хуже, чем не узнать вовсе.
"""

LANGUAGES = {
    "en": {"name": "English"},
    "de": {"name": "Deutsch"},
    "fr": {"name": "Français"},
    "es": {"name": "Español"},
    "uk": {"name": "Українська"},
    "ru": {"name": "Русский"},
}

UI = {
    "en": {
        "updated": "Last updated",
        "footer": "Hushwake is made by Kirill Sichushkin. Questions:",
        "titles": {"index": "Privacy Policy", "terms": "Terms of Use", "support": "Support"},
        "nav": {"privacy": "Privacy Policy", "terms": "Terms of Use", "support": "Support"},
    },
    "de": {
        "updated": "Zuletzt aktualisiert",
        "footer": "Hushwake stammt von Kirill Sichushkin. Fragen:",
        "titles": {"index": "Datenschutzerklärung", "terms": "Nutzungsbedingungen", "support": "Hilfe"},
        "nav": {"privacy": "Datenschutz", "terms": "Nutzungsbedingungen", "support": "Hilfe"},
    },
    "fr": {
        "updated": "Dernière mise à jour",
        "footer": "Hushwake est créé par Kirill Sichushkin. Questions :",
        "titles": {"index": "Politique de confidentialité", "terms": "Conditions d’utilisation", "support": "Aide"},
        "nav": {"privacy": "Confidentialité", "terms": "Conditions d’utilisation", "support": "Aide"},
    },
    "es": {
        "updated": "Última actualización",
        "footer": "Hushwake es obra de Kirill Sichushkin. Consultas:",
        "titles": {"index": "Política de privacidad", "terms": "Términos de uso", "support": "Ayuda"},
        "nav": {"privacy": "Privacidad", "terms": "Términos de uso", "support": "Ayuda"},
    },
    "uk": {
        "updated": "Востаннє оновлено",
        "footer": "Hushwake зробив Кирило Січушкін. Питання:",
        "titles": {"index": "Політика приватності", "terms": "Умови використання", "support": "Підтримка"},
        "nav": {"privacy": "Приватність", "terms": "Умови використання", "support": "Підтримка"},
    },
    "ru": {
        "updated": "Обновлено",
        "footer": "Hushwake сделал Кирилл Сичушкин. Вопросы:",
        "titles": {"index": "Политика конфиденциальности", "terms": "Условия использования", "support": "Поддержка"},
        "nav": {"privacy": "Конфиденциальность", "terms": "Условия использования", "support": "Поддержка"},
    },
}

PAGES = {}

# --------------------------------------------------------------------------- en

PAGES["en"] = {
    "index": """<div class="lede">
  <p><strong>Hushwake has no accounts, no servers and no analytics.</strong> It makes no network
  requests at all. The few things it remembers — your settings and your wake-up history — are
  stored on your iPhone and never leave it.</p>
</div>

<h2>What we collect</h2>
<p>Nothing. Hushwake contains no analytics SDKs, no advertising, no crash reporting and no
tracking of any kind. There is no code in the app that sends anything anywhere.</p>

<h2>What stays on your device</h2>
<ul>
  <li><strong>Wake-up history</strong> — for your recent wake-ups: the date, which wave was
  playing, how long you had set, and whether the wave woke you.</li>
  <li><strong>Settings</strong> — vibration strength, whether the tone is on, wave length,
  screen dimming, and the alarm or nap you set last.</li>
  <li><strong>Purchase state</strong> — whether the other waves are unlocked.</li>
</ul>
<p>All of it lives in the app's own storage and is removed when you delete the app.</p>

<h2>Notifications</h2>
<p>Hushwake asks for permission to send you notifications. It uses that permission for exactly
one thing: a <strong>backup alarm</strong>. Because iOS shuts down an app's haptic engine when the app
leaves the screen, Hushwake schedules a few local notifications at your wake-up time in case the app
is closed and the wave cannot play.</p>
<p>These notifications are created and delivered <strong>entirely on your iPhone</strong>. There
is no push server, no device token, and nothing about them reaches us or anyone else. If the app
is open on screen when they fire, they are suppressed and you never see them. You can decline
the permission or revoke it later in iOS Settings; the app keeps working, just without a
backup.</p>

<h2>What the app does not touch</h2>
<p>Hushwake does not use the microphone, the camera, motion sensors, location, contacts,
HealthKit or your calendar, and never asks for any of them. <strong>It does not track your
sleep</strong> — it cannot see you sleeping and does not try to.</p>

<h2>Sound and haptics</h2>
<p>The optional tone is generated on your device from a recipe in the app's code — nothing is
recorded and nothing is streamed.</p>

<h2>Purchases</h2>
<p>The one-time purchase is handled entirely by Apple through the App Store. Hushwake never sees
your payment details. We receive only the signed receipt Apple issues on your device, and we use
it for one thing: to know whether the other waves are unlocked. It is verified on your iPhone
and is not sent to us.</p>

<h2>Children</h2>
<p>Hushwake is rated 4+ and is suitable for all ages. It shows no advertising, contains no
third-party content, has no links out of the app except to these pages, and collects no
information from anyone. The only purchase is a single optional one, made through Apple with
whatever parental controls you have set.</p>

<h2>Your rights</h2>
<p>Because no personal data ever reaches us, there is nothing for us to export, correct or
delete on your behalf. Deleting the app removes everything Hushwake stored.</p>

<h2>Changes</h2>
<p>If this policy changes, the date at the top of this page changes with it. Material changes
will also be noted in the app's release notes.</p>

<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "terms": """<div class="lede">
  <p><strong>Hushwake is a clock.</strong> It is not a medical device, not a treatment and not a
  sleep tracker. It does not diagnose or treat insomnia, anxiety or any other condition, does not
  measure your sleep, and we make no claim that it does. If your sleep is troubling you, talk to
  a qualified professional rather than to an alarm app.</p>
</div>

<h2>How the alarm works — please read this</h2>
<p>The wake-up wave plays <strong>only while Hushwake is open on your screen</strong>. This is
not a defect and not something we can fix: iOS shuts down an app's haptic engine the moment the app
leaves the screen. Hushwake is designed around that — it stays open as a dim bedside clock, and
that is exactly what lets it play a real, app-shaped wave instead of a generic buzz.</p>
<p>So: plug the phone in, leave Hushwake open on screen, and put it where you will feel it. If
the app is closed or the phone restarts before your wake-up time, a <strong>backup
notification</strong> sounds instead, provided you allowed notifications and have not turned the
backup off.</p>
<p><strong>Try it before you depend on it.</strong> As with any alarm on any phone, do not make
Hushwake your only alarm for something you cannot miss — a flight, an exam — until you have
woken up with it a few times and know it works for you.</p>

<h2>Using the app</h2>
<p>Hushwake plays vibration and, optionally, a quiet tone at a time you set. You may use it for
personal, non-commercial purposes. You may not resell it, reverse-engineer it, or use it in a
way that breaks the law where you are.</p>

<h2>Health and safety</h2>
<p>Stop using Hushwake if it causes discomfort. Do not use the app while driving or operating
machinery. If the vibration is too strong or too weak, it can be adjusted in Settings, and the
optional tone can be turned on if vibration alone is not enough for you. Keep the volume moderate
if you use the tone with headphones.</p>

<h2>Purchases</h2>
<p>Hushwake is free to download and includes two full waves, with no ads and no time limits.
Unlocking the other waves is optional and costs a <strong>single one-time payment</strong>. It is
not a subscription: nothing renews and nothing is billed again.</p>
<p>The price is shown in the app in your local currency before you confirm anything. Payment is
charged to your Apple ID at confirmation of purchase. The purchase is tied to your Apple ID and
can be restored on your other devices from the purchase screen.</p>

<h2>Refunds</h2>
<p>Purchases are processed by Apple, so refunds are handled by Apple under the terms of the
App Store, not by us. Requests go through
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>

<h2>Warranty and liability</h2>
<p>Hushwake is provided as is, without warranties of any kind, to the fullest extent permitted by
law. To that same extent, we are not liable for indirect or consequential damages arising from
use of the app, including missed wake-ups. Nothing here limits liability that cannot be limited
by law, and you may have consumer rights in your country that these terms do not affect.</p>

<h2>Apple</h2>
<p>Apple is not a party to these terms and has no obligation to provide support for Hushwake.
Apple is a third-party beneficiary of these terms and may enforce them.</p>

<h2>Changes</h2>
<p>These terms may change; the date at the top of this page changes with them.</p>

<h2>Contact</h2>
<p><a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "support": """<div class="lede">
  <p>Something not working, or an idea for what should be? Write to
  <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a>. One person reads
  that inbox, usually within a couple of days.</p>
</div>

<h2>The alarm didn't go off</h2>
<p>Almost always this means the app was not on screen. The wave plays only while Hushwake is
open — iOS shuts down an app's haptic engine when the app leaves the screen. Leave the app on the night
screen, with the phone plugged in.</p>
<p>Turn on <strong>Wake me anyway</strong> in Settings and allow notifications, so that a backup
sounds if the app does get closed.</p>

<h2>Why does the app have to stay open?</h2>
<p>Because that is what makes the wave possible. An app that is closed can, at best, ask iOS to
post a notification, and the buzz you feel then is the system's — always the same shape, always
brief. Staying open lets Hushwake drive the Taptic Engine directly: a wave that starts below
noticing, builds for minutes, and keeps going until you stop it.</p>

<h2>I feel nothing</h2>
<p>Check that <strong>Settings → Sounds &amp; Haptics → System Haptics</strong> is on, and that
your phone is not in Low Power Mode, which weakens haptics. In the app, <strong>Strength</strong>
may be turned down. And make sure the phone is somewhere the vibration reaches you: on a soft
mattress it can be lost, on a bedside table it carries.</p>

<h2>The screen is almost black</h2>
<p>That is the night face doing its job — it dims so the light does not keep you awake, and
brightens again as the wave arrives. If you would rather it did not touch brightness at all, turn
off <strong>Dim the screen</strong> in Settings. Your brightness is always restored when you
leave the screen.</p>

<h2>Which wave should I pick?</h2>
<p>Start with <strong>Tide</strong>. If you wake before it finishes, try <strong>Dawn</strong>,
which stays below noticing for longer. If you sleep through, try <strong>Knock</strong>. Tap any
wave in the list to feel how it ends before you rely on it, and check the history: waves you have
slept through more than once are marked.</p>

<h2>Will it wake me if my phone is on silent?</h2>
<p>Yes. Vibration does not go through the ring switch, and the tone is off by default anyway.</p>

<h2>Will this drain my battery overnight?</h2>
<p>The screen stays on all night, so yes, noticeably — keep the phone on a charger. That is the
trade for a wave that actually plays.</p>

<h2>I bought the waves but they're still locked</h2>
<p>Open Settings in the app and tap <strong>Restore purchase</strong>, while signed in to the
Apple ID that made the purchase.</p>

<h2>Why is there no iPad or Mac version?</h2>
<p>Hushwake is built entirely around the Taptic Engine, which only iPhones have. Without it there
would be nothing left of the app. So it is iPhone only, on purpose.</p>

<h2>Where is my data?</h2>
<p>On your phone, and nowhere else. See the <a href="./">Privacy Policy</a>.</p>
""",
}

# --------------------------------------------------------------------------- de

PAGES["de"] = {
    "index": """<div class="lede">
  <p><strong>Hushwake hat keine Konten, keine Server und keine Analyse.</strong> Die App stellt
  überhaupt keine Netzwerkanfragen. Das Wenige, was sie sich merkt — deine Einstellungen und
  deinen Weckverlauf — liegt auf deinem iPhone und verlässt es nie.</p>
</div>

<h2>Was wir erheben</h2>
<p>Nichts. Hushwake enthält keine Analyse-SDKs, keine Werbung, kein Crash-Reporting und kein
Tracking jeglicher Art. Es gibt im Code keine Stelle, die irgendetwas irgendwohin sendet.</p>

<h2>Was auf deinem Gerät bleibt</h2>
<ul>
  <li><strong>Weckverlauf</strong> — zu deinen letzten Weckvorgängen: Datum, welche Welle lief,
  wie lange eingestellt war und ob die Welle dich geweckt hat.</li>
  <li><strong>Einstellungen</strong> — Vibrationsstärke, Ton an oder aus, Dauer der Welle,
  Abdunkeln des Displays und der zuletzt gestellte Wecker oder Kurzschlaf.</li>
  <li><strong>Kaufstatus</strong> — ob die übrigen Wellen freigeschaltet sind.</li>
</ul>
<p>Alles davon liegt im eigenen Speicher der App und verschwindet, wenn du sie löschst.</p>

<h2>Mitteilungen</h2>
<p>Hushwake bittet um die Erlaubnis für Mitteilungen und nutzt sie für genau eine Sache: einen
<strong>Ersatzwecker</strong>. Da iOS die Haptik-Engine einer App herunterfährt, sobald sie den Bildschirm verlässt, plant
Hushwake für deine Weckzeit einige lokale Mitteilungen — für den Fall, dass die App geschlossen
ist und die Welle nicht spielen kann.</p>
<p>Diese Mitteilungen entstehen und erscheinen <strong>vollständig auf deinem iPhone</strong>. Es
gibt keinen Push-Server, kein Gerätetoken, und nichts davon erreicht uns oder sonst jemanden. Ist
die App in dem Moment auf dem Bildschirm, werden sie unterdrückt und du siehst sie nie. Du kannst
die Erlaubnis verweigern oder später in den iOS-Einstellungen entziehen; die App funktioniert
weiter, nur eben ohne Absicherung.</p>

<h2>Was die App nicht anfasst</h2>
<p>Hushwake nutzt weder Mikrofon noch Kamera, keine Bewegungssensoren, keinen Standort, keine
Kontakte, kein HealthKit und keinen Kalender — und fragt nie danach. <strong>Die App trackt
deinen Schlaf nicht</strong>: sie kann dich nicht schlafen sehen und versucht es auch nicht.</p>

<h2>Ton und Haptik</h2>
<p>Der optionale Ton wird auf deinem Gerät aus einem Rezept im Code erzeugt — nichts ist
aufgenommen und nichts wird gestreamt.</p>

<h2>Käufe</h2>
<p>Der einmalige Kauf läuft vollständig über Apple und den App Store. Hushwake sieht deine
Zahlungsdaten nie. Wir erhalten nur den signierten Beleg, den Apple auf deinem Gerät ausstellt,
und nutzen ihn für eine einzige Frage: ob die übrigen Wellen freigeschaltet sind. Er wird auf
deinem iPhone geprüft und nicht an uns gesendet.</p>

<h2>Kinder</h2>
<p>Hushwake ist ab 4 Jahren freigegeben und für jedes Alter geeignet. Keine Werbung, keine
Inhalte Dritter, keine Links aus der App heraus außer auf diese Seiten, und es werden von
niemandem Daten erhoben. Der einzige Kauf ist ein einmaliger, optionaler, über Apple und die von
dir gesetzten Kindersicherungen.</p>

<h2>Deine Rechte</h2>
<p>Da uns nie personenbezogene Daten erreichen, gibt es für uns nichts zu exportieren, zu
berichtigen oder für dich zu löschen. Mit dem Löschen der App verschwindet alles, was Hushwake
gespeichert hat.</p>

<h2>Änderungen</h2>
<p>Ändert sich diese Erklärung, ändert sich das Datum oben mit. Wesentliche Änderungen stehen
zusätzlich in den Versionshinweisen der App.</p>

<h2>Kontakt</h2>
<p>Fragen zum Datenschutz: <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "terms": """<div class="lede">
  <p><strong>Hushwake ist eine Uhr.</strong> Kein Medizinprodukt, keine Behandlung und kein
  Schlaftracker. Die App diagnostiziert und behandelt weder Schlaflosigkeit noch Angst noch
  sonst etwas, misst deinen Schlaf nicht, und wir behaupten das auch nicht. Wenn dein Schlaf
  dich belastet, sprich mit einer Fachperson und nicht mit einer Wecker-App.</p>
</div>

<h2>Wie der Wecker funktioniert — bitte lesen</h2>
<p>Die Weckwelle spielt <strong>nur, solange Hushwake auf deinem Bildschirm offen ist</strong>.
Das ist kein Fehler und nichts, was wir beheben könnten: iOS fährt die Haptik-Engine einer App herunter,
sobald sie den Bildschirm verlässt. Hushwake ist genau darum herum gebaut — die App bleibt als
gedimmte Nachtuhr offen, und eben das erlaubt ihr, eine echte, selbst geformte Welle zu spielen
statt eines Standard-Brummens.</p>
<p>Also: Telefon laden, Hushwake offen lassen und so hinlegen, dass du die Vibration spürst. Ist
die App geschlossen oder startet das Telefon vor der Weckzeit neu, ertönt stattdessen eine
<strong>Ersatz-Mitteilung</strong> — sofern du Mitteilungen erlaubt und die Absicherung nicht
abgeschaltet hast.</p>
<p><strong>Probiere es aus, bevor du dich darauf verlässt.</strong> Wie bei jedem Wecker auf
jedem Telefon gilt: Mach Hushwake nicht zu deinem einzigen Wecker für etwas Unverzichtbares —
einen Flug, eine Prüfung — bevor du ein paar Mal damit aufgewacht bist.</p>

<h2>Nutzung der App</h2>
<p>Hushwake spielt Vibration und, wenn du willst, einen leisen Ton zu einer von dir gesetzten
Zeit. Du darfst sie privat und nicht-kommerziell nutzen. Du darfst sie nicht weiterverkaufen,
zurückentwickeln oder auf eine Weise nutzen, die an deinem Ort gegen das Gesetz verstößt.</p>

<h2>Gesundheit und Sicherheit</h2>
<p>Nutze Hushwake nicht weiter, wenn es unangenehm wird. Verwende die App nicht beim Fahren oder
beim Bedienen von Maschinen. Ist die Vibration zu stark oder zu schwach, lässt sie sich in den
Einstellungen anpassen; reicht sie dir allein nicht, kannst du den leisen Ton dazuschalten. Halte
die Lautstärke moderat, besonders mit Kopfhörern.</p>

<h2>Käufe</h2>
<p>Hushwake ist kostenlos und enthält zwei vollständige Wellen, ohne Werbung und ohne
Zeitlimit. Die übrigen Wellen freizuschalten ist optional und kostet eine <strong>einmalige
Zahlung</strong>. Kein Abo: nichts verlängert sich, nichts wird erneut abgebucht.</p>
<p>Der Preis wird in der App in deiner Währung angezeigt, bevor du irgendetwas bestätigst. Die
Abbuchung erfolgt bei Kaufbestätigung über deine Apple-ID. Der Kauf hängt an deiner Apple-ID und
lässt sich auf deinen anderen Geräten über den Kaufbildschirm wiederherstellen.</p>

<h2>Erstattungen</h2>
<p>Käufe werden von Apple abgewickelt, Erstattungen daher ebenfalls von Apple nach den
Bedingungen des App Store und nicht von uns. Anfragen laufen über
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>

<h2>Gewährleistung und Haftung</h2>
<p>Hushwake wird ohne jede Gewähr bereitgestellt, soweit gesetzlich zulässig. Im selben Umfang
haften wir nicht für mittelbare Schäden oder Folgeschäden aus der Nutzung der App, verschlafene
Termine eingeschlossen. Nichts hiervon beschränkt eine Haftung, die gesetzlich nicht
beschränkbar ist; Verbraucherrechte in deinem Land bleiben unberührt.</p>

<h2>Apple</h2>
<p>Apple ist nicht Partei dieser Bedingungen und nicht verpflichtet, Support für Hushwake zu
leisten. Apple ist begünstigter Dritter dieser Bedingungen und kann sie durchsetzen.</p>

<h2>Änderungen</h2>
<p>Diese Bedingungen können sich ändern; das Datum oben ändert sich mit.</p>

<h2>Kontakt</h2>
<p><a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "support": """<div class="lede">
  <p>Etwas geht nicht, oder du hast eine Idee? Schreib an
  <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a>. Dort liest ein Mensch,
  meist innerhalb von ein paar Tagen.</p>
</div>

<h2>Der Wecker hat nicht geweckt</h2>
<p>Fast immer heißt das: Die App war nicht auf dem Bildschirm. Die Welle spielt nur, solange
Hushwake offen ist — iOS fährt die Haptik-Engine einer App herunter, sobald sie den Bildschirm verlässt. Lass die App auf dem
Nachtbildschirm, das Telefon am Ladekabel.</p>
<p>Schalte in den Einstellungen <strong>Trotzdem wecken</strong> ein und erlaube Mitteilungen,
damit eine Absicherung ertönt, falls die App doch geschlossen wird.</p>

<h2>Warum muss die App offen bleiben?</h2>
<p>Weil erst das die Welle möglich macht. Eine geschlossene App kann iOS bestenfalls bitten, eine
Mitteilung zu zeigen — und die Vibration, die du dann spürst, gehört dem System: immer dieselbe
Form, immer kurz. Offen zu bleiben erlaubt Hushwake, die Taptic Engine direkt anzusteuern: eine
Welle, die unterhalb der Wahrnehmung beginnt, über Minuten wächst und weiterläuft, bis du sie
stoppst.</p>

<h2>Ich spüre nichts</h2>
<p>Prüfe, ob <strong>Einstellungen → Töne &amp; Haptik → Systemhaptik</strong> an ist und dein
Telefon nicht im Stromsparmodus läuft, der die Haptik abschwächt. In der App könnte
<strong>Stärke</strong> heruntergedreht sein. Und leg das Telefon dorthin, wo die Vibration dich
erreicht: in einer weichen Matratze verschwindet sie, auf dem Nachttisch trägt sie.</p>

<h2>Der Bildschirm ist fast schwarz</h2>
<p>Das ist das Nachtzifferblatt: Es dimmt, damit dich das Licht nicht wachhält, und hellt mit der
Welle wieder auf. Wenn die App die Helligkeit gar nicht anfassen soll, schalte in den
Einstellungen <strong>Display abdunkeln</strong> aus. Beim Verlassen des Bildschirms wird deine
Helligkeit immer zurückgesetzt.</p>

<h2>Welche Welle soll ich nehmen?</h2>
<p>Fang mit <strong>Flut</strong> an. Wachst du auf, bevor sie fertig ist, probier
<strong>Dämmerung</strong> — die bleibt länger unterhalb der Wahrnehmung. Verschläfst du, probier
<strong>Klopfen</strong>. Tippe jede Welle in der Liste an, um zu spüren, wie sie endet, und sieh
in den Verlauf: Wellen, die du mehr als einmal verschlafen hast, sind markiert.</p>

<h2>Weckt es mich, wenn das Telefon lautlos ist?</h2>
<p>Ja. Vibration hängt nicht am Klingelschalter, und der Ton ist ohnehin standardmäßig aus.</p>

<h2>Zieht das nachts den Akku leer?</h2>
<p>Der Bildschirm bleibt die ganze Nacht an, also ja, spürbar — lass das Telefon am Ladegerät.
Das ist der Preis für eine Welle, die wirklich spielt.</p>

<h2>Ich habe gekauft, es ist trotzdem gesperrt</h2>
<p>Öffne die Einstellungen in der App und tippe auf <strong>Kauf wiederherstellen</strong> —
angemeldet mit der Apple-ID, die den Kauf getätigt hat.</p>

<h2>Warum gibt es keine iPad- oder Mac-Version?</h2>
<p>Hushwake ist vollständig um die Taptic Engine herum gebaut, die es nur im iPhone gibt. Ohne
sie bliebe von der App nichts übrig. Deshalb: nur iPhone, mit Absicht.</p>

<h2>Wo sind meine Daten?</h2>
<p>Auf deinem Telefon und sonst nirgends. Siehe die
<a href="./">Datenschutzerklärung</a>.</p>
""",
}

# --------------------------------------------------------------------------- fr

PAGES["fr"] = {
    "index": """<div class="lede">
  <p><strong>Hushwake n’a ni comptes, ni serveurs, ni analyse.</strong> L’app ne fait aucune
  requête réseau. Le peu qu’elle retient — vos réglages et votre historique de réveils — reste
  sur votre iPhone et n’en sort jamais.</p>
</div>

<h2>Ce que nous collectons</h2>
<p>Rien. Hushwake ne contient aucun SDK d’analyse, aucune publicité, aucun rapport de plantage
et aucun pistage d’aucune sorte. Il n’y a dans le code aucun endroit qui envoie quoi que ce soit
où que ce soit.</p>

<h2>Ce qui reste sur votre appareil</h2>
<ul>
  <li><strong>Historique des réveils</strong> — pour vos réveils récents : la date, la vague qui
  jouait, la durée réglée et si la vague vous a réveillé.</li>
  <li><strong>Réglages</strong> — intensité de la vibration, son activé ou non, durée de la
  vague, assombrissement de l’écran, et le réveil ou la sieste réglés en dernier.</li>
  <li><strong>État d’achat</strong> — si les autres vagues sont débloquées.</li>
</ul>
<p>Tout cela vit dans le stockage propre à l’app et disparaît quand vous la supprimez.</p>

<h2>Notifications</h2>
<p>Hushwake demande l’autorisation d’envoyer des notifications et s’en sert pour une seule
chose : un <strong>réveil de secours</strong>. Comme iOS coupe le moteur haptique d’une app dès qu’elle
quitte l’écran, Hushwake programme quelques notifications locales à l’heure de votre réveil, au cas
où l’app serait fermée et la vague ne pourrait pas jouer.</p>
<p>Ces notifications sont créées et délivrées <strong>entièrement sur votre iPhone</strong>. Pas
de serveur push, pas de jeton d’appareil, et rien de tout cela ne nous parvient ni ne parvient à
qui que ce soit. Si l’app est à l’écran à ce moment-là, elles sont supprimées et vous ne les
voyez jamais. Vous pouvez refuser l’autorisation ou la retirer plus tard dans les réglages
d’iOS ; l’app continue de fonctionner, simplement sans filet.</p>

<h2>Ce à quoi l’app ne touche pas</h2>
<p>Hushwake n’utilise ni le micro, ni l’appareil photo, ni les capteurs de mouvement, ni la
localisation, ni les contacts, ni HealthKit, ni votre calendrier, et ne les demande jamais.
<strong>L’app ne suit pas votre sommeil</strong> : elle ne peut pas vous voir dormir et
n’essaie pas.</p>

<h2>Son et haptique</h2>
<p>Le son facultatif est généré sur votre appareil à partir d’une recette inscrite dans le code —
rien n’est enregistré, rien n’est diffusé.</p>

<h2>Achats</h2>
<p>L’achat unique est entièrement géré par Apple via l’App Store. Hushwake ne voit jamais vos
informations de paiement. Nous recevons uniquement le reçu signé qu’Apple émet sur votre
appareil, et il ne sert qu’à une chose : savoir si les autres vagues sont débloquées. Il est
vérifié sur votre iPhone et ne nous est pas transmis.</p>

<h2>Enfants</h2>
<p>Hushwake est classée 4+ et convient à tout âge. Aucune publicité, aucun contenu tiers, aucun
lien sortant hormis vers ces pages, et aucune information collectée sur qui que ce soit. Le seul
achat est unique et facultatif, effectué via Apple avec les contrôles parentaux que vous avez
définis.</p>

<h2>Vos droits</h2>
<p>Comme aucune donnée personnelle ne nous parvient, nous n’avons rien à exporter, corriger ou
supprimer pour vous. Supprimer l’app efface tout ce que Hushwake avait enregistré.</p>

<h2>Modifications</h2>
<p>Si cette politique change, la date en haut de page change avec elle. Les changements
importants figurent aussi dans les notes de version.</p>

<h2>Contact</h2>
<p>Questions sur la confidentialité :
<a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "terms": """<div class="lede">
  <p><strong>Hushwake est une horloge.</strong> Ni dispositif médical, ni traitement, ni suivi du
  sommeil. L’app ne diagnostique ni ne traite l’insomnie, l’anxiété ou quoi que ce soit d’autre,
  ne mesure pas votre sommeil, et nous ne prétendons pas le contraire. Si votre sommeil vous
  inquiète, parlez-en à un professionnel plutôt qu’à une app de réveil.</p>
</div>

<h2>Comment fonctionne le réveil — à lire</h2>
<p>La vague de réveil ne joue <strong>que tant que Hushwake est ouverte à l’écran</strong>. Ce
n’est pas un défaut et ce n’est pas quelque chose que nous pouvons corriger : iOS coupe le moteur
haptique d’une app dès qu’elle quitte l’écran. Hushwake est conçue autour de cela —
elle reste ouverte en horloge de chevet tamisée, et c’est précisément ce qui lui permet de jouer
une vraie vague façonnée par l’app plutôt qu’un bourdonnement générique.</p>
<p>Donc : branchez le téléphone, laissez Hushwake ouverte et posez-la là où vous sentirez la
vibration. Si l’app est fermée ou si le téléphone redémarre avant l’heure, une
<strong>notification de secours</strong> sonne à la place, à condition d’avoir autorisé les
notifications et de ne pas avoir désactivé le filet.</p>
<p><strong>Essayez avant d’en dépendre.</strong> Comme pour n’importe quel réveil sur n’importe
quel téléphone : ne faites pas de Hushwake votre seul réveil pour quelque chose d’essentiel —
un avion, un examen — avant de vous être réveillé avec elle plusieurs fois.</p>

<h2>Utilisation de l’app</h2>
<p>Hushwake joue une vibration et, si vous le souhaitez, un son discret à l’heure que vous
réglez. Vous pouvez l’utiliser à des fins personnelles et non commerciales. Vous ne pouvez pas la
revendre, la rétro-concevoir, ni l’utiliser d’une manière contraire à la loi chez vous.</p>

<h2>Santé et sécurité</h2>
<p>Cessez d’utiliser Hushwake si cela devient inconfortable. N’utilisez pas l’app en conduisant
ou en manœuvrant une machine. Si la vibration est trop forte ou trop faible, elle se règle dans
les réglages ; si elle ne suffit pas seule, vous pouvez activer le son discret. Gardez un volume
modéré, surtout au casque.</p>

<h2>Achats</h2>
<p>Hushwake est gratuite au téléchargement et comprend deux vagues complètes, sans publicité ni
limite de temps. Débloquer les autres vagues est facultatif et coûte un <strong>paiement
unique</strong>. Ce n’est pas un abonnement : rien ne se renouvelle, rien n’est facturé à
nouveau.</p>
<p>Le prix s’affiche dans l’app, dans votre devise, avant toute confirmation. Le paiement est
prélevé sur votre identifiant Apple à la confirmation. L’achat est lié à votre identifiant Apple
et se restaure sur vos autres appareils depuis l’écran d’achat.</p>

<h2>Remboursements</h2>
<p>Les achats sont traités par Apple, les remboursements aussi, selon les conditions de l’App
Store et non les nôtres. Les demandes passent par
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>

<h2>Garantie et responsabilité</h2>
<p>Hushwake est fournie en l’état, sans garantie d’aucune sorte, dans toute la mesure permise par
la loi. Dans la même mesure, nous ne sommes pas responsables des dommages indirects ou
consécutifs liés à l’usage de l’app, y compris un réveil manqué. Rien ici ne limite une
responsabilité que la loi ne permet pas de limiter, et vos droits de consommateur dans votre pays
ne sont pas affectés.</p>

<h2>Apple</h2>
<p>Apple n’est pas partie à ces conditions et n’a aucune obligation d’assurer le support de
Hushwake. Apple en est tiers bénéficiaire et peut les faire appliquer.</p>

<h2>Modifications</h2>
<p>Ces conditions peuvent changer ; la date en haut de page change avec elles.</p>

<h2>Contact</h2>
<p><a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "support": """<div class="lede">
  <p>Quelque chose ne marche pas, ou une idée de ce qui devrait exister ? Écrivez à
  <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a>. Une personne lit cette
  boîte, en général sous quelques jours.</p>
</div>

<h2>Le réveil n’a pas sonné</h2>
<p>Presque toujours, cela veut dire que l’app n’était pas à l’écran. La vague ne joue que tant
que Hushwake est ouverte — iOS coupe le moteur haptique d’une app dès qu’elle quitte l’écran. Laissez l’app sur
l’écran de nuit, téléphone branché.</p>
<p>Activez <strong>Me réveiller quand même</strong> dans les réglages et autorisez les
notifications, pour qu’un secours sonne si l’app se ferme quand même.</p>

<h2>Pourquoi l’app doit-elle rester ouverte ?</h2>
<p>Parce que c’est ce qui rend la vague possible. Une app fermée peut au mieux demander à iOS
d’afficher une notification, et la vibration que vous sentez alors appartient au système :
toujours la même forme, toujours brève. Rester ouverte permet à Hushwake de piloter directement
le Taptic Engine : une vague qui commence sous le seuil de perception, monte pendant des minutes
et continue jusqu’à ce que vous l’arrêtiez.</p>

<h2>Je ne sens rien</h2>
<p>Vérifiez que <strong>Réglages → Sons et vibrations → Vibrations système</strong> est activé et
que le téléphone n’est pas en mode économie d’énergie, qui affaiblit l’haptique. Dans l’app,
<strong>Intensité</strong> peut être baissée. Et posez le téléphone là où la vibration vous
atteint : dans un matelas moelleux elle se perd, sur une table de chevet elle porte.</p>

<h2>L’écran est presque noir</h2>
<p>C’est le cadran de nuit qui fait son travail : il s’assombrit pour que la lumière ne vous
tienne pas éveillé, et remonte avec la vague. Si vous préférez que l’app ne touche pas du tout à
la luminosité, désactivez <strong>Assombrir l’écran</strong> dans les réglages. Votre luminosité
est toujours rétablie en quittant l’écran.</p>

<h2>Quelle vague choisir ?</h2>
<p>Commencez par <strong>Marée</strong>. Si vous vous réveillez avant la fin, essayez
<strong>Aube</strong>, qui reste plus longtemps sous le seuil. Si vous dormez malgré tout, essayez
<strong>Frappe</strong>. Touchez n’importe quelle vague dans la liste pour sentir sa fin avant de
lui faire confiance, et regardez l’historique : les vagues que vous avez manquées plus d’une fois
sont marquées.</p>

<h2>Est-ce que ça me réveille si le téléphone est en silencieux ?</h2>
<p>Oui. La vibration ne passe pas par le bouton silencieux, et le son est de toute façon
désactivé par défaut.</p>

<h2>Est-ce que ça vide la batterie la nuit ?</h2>
<p>L’écran reste allumé toute la nuit, donc oui, sensiblement — gardez le téléphone sur son
chargeur. C’est le prix d’une vague qui joue vraiment.</p>

<h2>J’ai acheté les vagues mais elles restent verrouillées</h2>
<p>Ouvrez les réglages dans l’app et touchez <strong>Restaurer l’achat</strong>, connecté avec
l’identifiant Apple qui a fait l’achat.</p>

<h2>Pourquoi pas de version iPad ou Mac ?</h2>
<p>Hushwake est entièrement construite autour du Taptic Engine, que seuls les iPhone possèdent.
Sans lui, il ne resterait rien de l’app. Donc iPhone uniquement, volontairement.</p>

<h2>Où sont mes données ?</h2>
<p>Sur votre téléphone, et nulle part ailleurs. Voir la
<a href="./">politique de confidentialité</a>.</p>
""",
}

# --------------------------------------------------------------------------- es

PAGES["es"] = {
    "index": """<div class="lede">
  <p><strong>Hushwake no tiene cuentas, ni servidores, ni analítica.</strong> No hace ninguna
  petición de red. Lo poco que recuerda — tus ajustes y tu historial de despertares — se guarda
  en tu iPhone y nunca sale de ahí.</p>
</div>

<h2>Qué recogemos</h2>
<p>Nada. Hushwake no incluye SDK de analítica, ni publicidad, ni informes de fallos, ni
seguimiento de ningún tipo. No hay en el código ni un punto que envíe nada a ninguna parte.</p>

<h2>Qué se queda en tu dispositivo</h2>
<ul>
  <li><strong>Historial de despertares</strong> — de tus despertares recientes: la fecha, qué ola
  sonaba, cuánto tiempo habías puesto y si la ola te despertó.</li>
  <li><strong>Ajustes</strong> — intensidad de la vibración, tono activado o no, duración de la
  ola, atenuación de pantalla y la alarma o siesta que pusiste por última vez.</li>
  <li><strong>Estado de compra</strong> — si las demás olas están desbloqueadas.</li>
</ul>
<p>Todo eso vive en el almacenamiento propio de la app y desaparece al eliminarla.</p>

<h2>Notificaciones</h2>
<p>Hushwake pide permiso para enviarte notificaciones y lo usa para una sola cosa: una
<strong>alarma de respaldo</strong>. Como iOS apaga el motor háptico de una app en cuanto sale de pantalla,
Hushwake programa unas cuantas notificaciones locales a tu hora de despertar, por si la app está
cerrada y la ola no puede sonar.</p>
<p>Esas notificaciones se crean y se entregan <strong>íntegramente en tu iPhone</strong>. No hay
servidor push, ni token de dispositivo, y nada de eso llega a nosotros ni a nadie. Si la app está
en pantalla en ese momento, quedan suprimidas y nunca las ves. Puedes rechazar el permiso o
retirarlo después en los Ajustes de iOS; la app sigue funcionando, solo que sin red de
seguridad.</p>

<h2>Lo que la app no toca</h2>
<p>Hushwake no usa el micrófono, la cámara, los sensores de movimiento, la ubicación, los
contactos, HealthKit ni tu calendario, y nunca los pide. <strong>No monitoriza tu sueño</strong>:
no puede verte dormir y no lo intenta.</p>

<h2>Sonido y háptica</h2>
<p>El tono opcional se genera en tu dispositivo a partir de una receta escrita en el código: no
hay nada grabado ni nada en streaming.</p>

<h2>Compras</h2>
<p>La compra única la gestiona Apple por completo a través del App Store. Hushwake nunca ve tus
datos de pago. Solo recibimos el recibo firmado que Apple emite en tu dispositivo, y sirve para
una única cosa: saber si las demás olas están desbloqueadas. Se verifica en tu iPhone y no se nos
envía.</p>

<h2>Menores</h2>
<p>Hushwake tiene clasificación 4+ y es apta para cualquier edad. Sin publicidad, sin contenido
de terceros, sin enlaces fuera de la app salvo a estas páginas, y sin recoger información de
nadie. La única compra es única y opcional, hecha a través de Apple con los controles parentales
que tengas configurados.</p>

<h2>Tus derechos</h2>
<p>Como ningún dato personal llega hasta nosotros, no hay nada que podamos exportar, corregir o
eliminar en tu nombre. Eliminar la app borra todo lo que Hushwake había guardado.</p>

<h2>Cambios</h2>
<p>Si esta política cambia, la fecha de arriba cambia con ella. Los cambios relevantes se indican
también en las notas de versión.</p>

<h2>Contacto</h2>
<p>Dudas sobre privacidad:
<a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "terms": """<div class="lede">
  <p><strong>Hushwake es un reloj.</strong> No es un producto sanitario, ni un tratamiento, ni un
  monitor de sueño. No diagnostica ni trata el insomnio, la ansiedad ni ninguna otra condición,
  no mide tu sueño, y no afirmamos lo contrario. Si tu sueño te preocupa, habla con un
  profesional y no con una app de alarma.</p>
</div>

<h2>Cómo funciona la alarma — léelo</h2>
<p>La ola de despertar suena <strong>solo mientras Hushwake está abierta en pantalla</strong>. No
es un defecto ni algo que podamos arreglar: iOS apaga el motor háptico de una app en cuanto sale
de pantalla. Hushwake está construida en torno a eso: se queda abierta como reloj de mesilla
atenuado, y eso es justo lo que le permite reproducir una ola de verdad, diseñada por la app, en
lugar de un zumbido genérico.</p>
<p>Así que: enchufa el teléfono, deja Hushwake abierta y ponla donde notes la vibración. Si la
app se cierra o el teléfono se reinicia antes de la hora, suena en su lugar una
<strong>notificación de respaldo</strong>, siempre que hayas permitido las notificaciones y no
hayas desactivado el respaldo.</p>
<p><strong>Pruébala antes de depender de ella.</strong> Como con cualquier alarma en cualquier
teléfono: no hagas de Hushwake tu única alarma para algo que no puedes perder — un vuelo, un
examen — hasta que te hayas despertado con ella unas cuantas veces.</p>

<h2>Uso de la app</h2>
<p>Hushwake reproduce vibración y, si quieres, un tono discreto a la hora que fijes. Puedes
usarla con fines personales y no comerciales. No puedes revenderla, aplicarle ingeniería inversa
ni usarla de un modo que infrinja la ley donde estés.</p>

<h2>Salud y seguridad</h2>
<p>Deja de usar Hushwake si te resulta molesta. No uses la app mientras conduces o manejas
maquinaria. Si la vibración es demasiado fuerte o demasiado débil, se ajusta en los Ajustes; si
por sí sola no te basta, puedes activar el tono discreto. Mantén un volumen moderado, sobre todo
con auriculares.</p>

<h2>Compras</h2>
<p>Hushwake es gratis e incluye dos olas completas, sin anuncios ni límites de tiempo.
Desbloquear las demás es opcional y cuesta un <strong>único pago</strong>. No es una suscripción:
nada se renueva y nada se vuelve a cobrar.</p>
<p>El precio se muestra en la app en tu moneda antes de que confirmes nada. El cargo se hace a tu
ID de Apple al confirmar la compra. La compra queda ligada a tu ID de Apple y se puede restaurar
en tus otros dispositivos desde la pantalla de compra.</p>

<h2>Reembolsos</h2>
<p>Las compras las procesa Apple, así que los reembolsos también los gestiona Apple según los
términos del App Store, no nosotros. Las solicitudes van por
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>

<h2>Garantía y responsabilidad</h2>
<p>Hushwake se ofrece tal cual, sin garantías de ningún tipo, en la máxima medida permitida por
la ley. En esa misma medida, no somos responsables de daños indirectos o derivados del uso de la
app, incluidos los despertares que no ocurran. Nada de esto limita responsabilidades que la ley
no permita limitar, y tus derechos como consumidor en tu país no se ven afectados.</p>

<h2>Apple</h2>
<p>Apple no es parte de estos términos y no tiene obligación de dar soporte a Hushwake. Apple es
tercero beneficiario de estos términos y puede hacerlos valer.</p>

<h2>Cambios</h2>
<p>Estos términos pueden cambiar; la fecha de arriba cambia con ellos.</p>

<h2>Contacto</h2>
<p><a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "support": """<div class="lede">
  <p>¿Algo no funciona, o tienes una idea de lo que debería existir? Escribe a
  <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a>. Ese buzón lo lee una
  persona, normalmente en un par de días.</p>
</div>

<h2>La alarma no sonó</h2>
<p>Casi siempre significa que la app no estaba en pantalla. La ola solo suena mientras Hushwake
está abierta: iOS apaga el motor háptico de una app en cuanto sale de pantalla. Deja la app en la pantalla
nocturna y el teléfono enchufado.</p>
<p>Activa <strong>Despiértame igualmente</strong> en los ajustes y permite las notificaciones,
para que suene un respaldo si la app acaba cerrándose.</p>

<h2>¿Por qué tiene que quedarse abierta la app?</h2>
<p>Porque es lo que hace posible la ola. Una app cerrada, como mucho, puede pedirle a iOS que
muestre una notificación, y la vibración que notas entonces es la del sistema: siempre la misma
forma, siempre breve. Quedarse abierta permite a Hushwake gobernar directamente el Taptic Engine:
una ola que empieza por debajo de lo perceptible, crece durante minutos y sigue hasta que la
paras.</p>

<h2>No noto nada</h2>
<p>Comprueba que <strong>Ajustes → Sonidos y vibraciones → Vibración del sistema</strong> esté
activado y que el teléfono no esté en modo de bajo consumo, que debilita la háptica. En la app,
<strong>Intensidad</strong> puede estar baja. Y deja el teléfono donde la vibración te llegue: en
un colchón blando se pierde, en la mesilla se transmite.</p>

<h2>La pantalla está casi negra</h2>
<p>Es la esfera nocturna haciendo su trabajo: se atenúa para que la luz no te desvele y vuelve a
iluminarse con la ola. Si prefieres que la app no toque el brillo en absoluto, desactiva
<strong>Atenuar la pantalla</strong> en los ajustes. Tu brillo siempre se restaura al salir de la
pantalla.</p>

<h2>¿Qué ola elijo?</h2>
<p>Empieza por <strong>Marea</strong>. Si te despiertas antes de que termine, prueba
<strong>Alba</strong>, que se mantiene más tiempo por debajo de lo perceptible. Si te duermes,
prueba <strong>Golpe</strong>. Toca cualquier ola de la lista para sentir cómo acaba antes de
confiar en ella, y mira el historial: las olas con las que te has dormido más de una vez están
marcadas.</p>

<h2>¿Me despierta si el teléfono está en silencio?</h2>
<p>Sí. La vibración no pasa por el interruptor de silencio, y el tono viene desactivado por
defecto de todos modos.</p>

<h2>¿Me gastará la batería por la noche?</h2>
<p>La pantalla se queda encendida toda la noche, así que sí, de forma notable: deja el teléfono
cargando. Es el precio de una ola que suena de verdad.</p>

<h2>Compré las olas y siguen bloqueadas</h2>
<p>Abre los ajustes de la app y toca <strong>Restaurar compra</strong>, con la sesión iniciada en
el ID de Apple con el que compraste.</p>

<h2>¿Por qué no hay versión para iPad o Mac?</h2>
<p>Hushwake está construida por completo alrededor del Taptic Engine, que solo tienen los iPhone.
Sin él no quedaría nada de la app. Así que solo iPhone, a propósito.</p>

<h2>¿Dónde están mis datos?</h2>
<p>En tu teléfono y en ningún otro sitio. Consulta la
<a href="./">política de privacidad</a>.</p>
""",
}

# --------------------------------------------------------------------------- uk

PAGES["uk"] = {
    "index": """<div class="lede">
  <p><strong>У Hushwake немає ні акаунтів, ні серверів, ні аналітики.</strong> Застосунок узагалі
  не робить мережевих запитів. Те небагато, що він пам’ятає — ваші налаштування та історію
  підйомів, — зберігається на вашому iPhone і ніколи його не залишає.</p>
</div>

<h2>Що ми збираємо</h2>
<p>Нічого. У Hushwake немає ні SDK аналітики, ні реклами, ні звітів про збої, ні стеження
будь-якого штибу. У коді немає жодного місця, яке щось кудись надсилає.</p>

<h2>Що лишається на вашому пристрої</h2>
<ul>
  <li><strong>Історія підйомів</strong> — про останні підйоми: дата, яка хвиля грала, скільки
  було заведено і чи розбудила хвиля.</li>
  <li><strong>Налаштування</strong> — сила вібрації, увімкнений тон чи ні, тривалість хвилі,
  притемнення екрана та останні заведені будильник або дрімка.</li>
  <li><strong>Стан покупки</strong> — чи відкрито решту хвиль.</li>
</ul>
<p>Усе це живе у власному сховищі застосунку й зникає, коли ви його видаляєте.</p>

<h2>Сповіщення</h2>
<p>Hushwake просить дозвіл на сповіщення й використовує його рівно для однієї речі —
<strong>запасного будильника</strong>. Оскільки iOS вимикає тактильний рушій застосунку, щойно той
залишає екран, Hushwake планує кілька локальних сповіщень на час вашого підйому — на випадок, якщо
застосунок закрито й хвиля зіграти не зможе.</p>
<p>Ці сповіщення створюються і показуються <strong>повністю на вашому iPhone</strong>. Ні
push-сервера, ні токена пристрою, і нічого з цього не потрапляє ні до нас, ні до когось іще.
Якщо в цей момент застосунок на екрані, вони придушуються і ви їх не бачите. Дозвіл можна не
давати або відкликати пізніше в налаштуваннях iOS; застосунок працюватиме далі, просто без
підстраховки.</p>

<h2>Чого застосунок не торкається</h2>
<p>Hushwake не використовує ні мікрофон, ні камеру, ні датчики руху, ні геопозицію, ні контакти,
ні HealthKit, ні календар — і ніколи їх не просить. <strong>Він не стежить за вашим сном</strong>:
він не може бачити, як ви спите, і не намагається.</p>

<h2>Звук і тактильність</h2>
<p>Необов’язковий тон синтезується на вашому пристрої за рецептом у коді — нічого не записано
й нічого не транслюється.</p>

<h2>Покупки</h2>
<p>Разову покупку повністю опрацьовує Apple через App Store. Hushwake ніколи не бачить ваших
платіжних даних. Ми отримуємо лише підписаний чек, який Apple видає на вашому пристрої, і
використовуємо його для однієї речі: дізнатися, чи відкрито решту хвиль. Він перевіряється на
вашому iPhone і нам не надсилається.</p>

<h2>Діти</h2>
<p>Hushwake має рейтинг 4+ і підходить будь-якому віку. Ні реклами, ні стороннього вмісту, ні
посилань назовні, крім цих сторінок, і жодних даних ні про кого. Єдина покупка — разова
й необов’язкова, через Apple і з вашими батьківськими обмеженнями.</p>

<h2>Ваші права</h2>
<p>Оскільки персональні дані до нас не потрапляють, нам нічого експортувати, виправляти чи
видаляти за вас. Видалення застосунку прибирає все, що Hushwake зберігав.</p>

<h2>Зміни</h2>
<p>Якщо ця політика зміниться, дата вгорі сторінки зміниться разом із нею. Про суттєві зміни
буде сказано і в нотатках до версії.</p>

<h2>Контакт</h2>
<p>Питання про приватність:
<a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "terms": """<div class="lede">
  <p><strong>Hushwake — це годинник.</strong> Не медичний пристрій, не лікування і не трекер сну.
  Застосунок не діагностує й не лікує безсоння, тривожність чи будь-що інше, не вимірює ваш сон,
  і ми цього не стверджуємо. Якщо сон вас непокоїть, говоріть із фахівцем, а не з будильником.</p>
</div>

<h2>Як працює будильник — прочитайте</h2>
<p>Хвиля пробудження грає <strong>лише доки Hushwake відкритий на екрані</strong>. Це не дефект
і не те, що ми можемо виправити: iOS вимикає тактильний рушій застосунку, щойно той залишає екран.
Hushwake побудований саме навколо цього — він лишається відкритим як притемнений приліжковий
годинник, і саме це дозволяє йому грати справжню, задану застосунком хвилю, а не типове
дзижчання.</p>
<p>Отже: поставте телефон на зарядку, лишіть Hushwake відкритим і покладіть так, щоб відчувати
вібрацію. Якщо застосунок закрито або телефон перезавантажився до часу підйому, замість хвилі
пролунає <strong>запасне сповіщення</strong> — за умови, що ви дозволили сповіщення й не
вимкнули підстраховку.</p>
<p><strong>Спробуйте, перш ніж покладатися.</strong> Як і з будь-яким будильником на будь-якому
телефоні: не робіть Hushwake єдиним будильником на щось важливе — літак, іспит — доки не
прокинулися з ним кілька разів.</p>

<h2>Користування застосунком</h2>
<p>Hushwake відтворює вібрацію і, за бажанням, тихий тон у заданий вами час. Ви можете
користуватися ним в особистих, некомерційних цілях. Не можна перепродавати його, робити зворотну
розробку чи використовувати способом, що порушує закон там, де ви є.</p>

<h2>Здоров’я і безпека</h2>
<p>Припиніть користуватися Hushwake, якщо стає незручно. Не користуйтеся застосунком за кермом
або керуючи механізмами. Якщо вібрація надто сильна чи надто слабка, її можна налаштувати; якщо
самої вібрації замало, можна ввімкнути тихий тон. Тримайте помірну гучність, особливо
в навушниках.</p>

<h2>Покупки</h2>
<p>Hushwake безкоштовний і містить дві повноцінні хвилі, без реклами й часових обмежень.
Відкрити решту — за бажанням, за <strong>один разовий платіж</strong>. Це не підписка: ніщо
не поновлюється і не списується повторно.</p>
<p>Ціна показується в застосунку у вашій валюті до будь-якого підтвердження. Кошти списуються
з вашого Apple ID у момент підтвердження. Покупка прив’язана до Apple ID і відновлюється
на інших ваших пристроях з екрана покупки.</p>

<h2>Повернення коштів</h2>
<p>Покупки опрацьовує Apple, тож і повернення — теж Apple, за умовами App Store, а не нами.
Запити подаються через
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>

<h2>Гарантії та відповідальність</h2>
<p>Hushwake надається «як є», без жодних гарантій, у межах, дозволених законом. У тих самих межах
ми не відповідаємо за непрямі або похідні збитки від користування застосунком, включно
з проспаними підйомами. Ніщо тут не обмежує відповідальність, яку закон обмежувати не дозволяє,
а ваші споживчі права у вашій країні лишаються чинними.</p>

<h2>Apple</h2>
<p>Apple не є стороною цих умов і не зобов’язана надавати підтримку Hushwake. Apple є третьою
стороною-вигодонабувачем цих умов і може вимагати їх виконання.</p>

<h2>Зміни</h2>
<p>Ці умови можуть змінюватися; дата вгорі сторінки змінюється разом із ними.</p>

<h2>Контакт</h2>
<p><a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "support": """<div class="lede">
  <p>Щось не працює або є ідея, як має бути? Напишіть на
  <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a>. Цю скриньку читає людина,
  зазвичай протягом кількох днів.</p>
</div>

<h2>Будильник не спрацював</h2>
<p>Майже завжди це означає, що застосунок не був на екрані. Хвиля грає лише доки Hushwake
відкритий — iOS вимикає тактильний рушій застосунку, щойно той залишає екран. Лишайте застосунок на нічному
екрані, а телефон на зарядці.</p>
<p>Увімкніть <strong>Розбудити попри все</strong> в налаштуваннях і дозвольте сповіщення, щоб
підстраховка пролунала, якщо застосунок усе ж закриють.</p>

<h2>Чому застосунок має лишатися відкритим?</h2>
<p>Бо саме це робить хвилю можливою. Закритий застосунок у кращому разі може попросити iOS
показати сповіщення, і вібрація, яку ви тоді відчуваєте, належить системі: завжди однакової
форми, завжди коротка. Лишаючись відкритим, Hushwake керує Taptic Engine напряму: хвиля
починається нижче порога відчуття, наростає хвилинами й триває, доки ви її не зупините.</p>

<h2>Я нічого не відчуваю</h2>
<p>Перевірте, що <strong>Параметри → Звуки та тактильні сигнали → Системна тактильність</strong>
увімкнено і телефон не в режимі енергозбереження, який послаблює тактильність. У застосунку може
бути прикручена <strong>Сила</strong>. І покладіть телефон туди, де вібрація до вас дійде:
у м’якому матраці вона губиться, на тумбочці — передається.</p>

<h2>Екран майже чорний</h2>
<p>Це нічний циферблат робить свою справу: він гасне, щоб світло не тримало вас без сну, і
світлішає разом із хвилею. Якщо не хочете, щоб застосунок узагалі торкався яскравості, вимкніть
<strong>Притемнювати екран</strong> у налаштуваннях. Ваша яскравість завжди повертається під час
виходу з екрана.</p>

<h2>Яку хвилю обрати?</h2>
<p>Почніть із <strong>Припливу</strong>. Якщо прокидаєтеся до його кінця, спробуйте
<strong>Світанок</strong> — він довше лишається нижче порога. Якщо просинаєте, спробуйте
<strong>Стук</strong>. Торкніться будь-якої хвилі в списку, щоб відчути її кінець, перш ніж на
неї покладатися, і загляньте в історію: хвилі, які ви проспали не раз, позначені.</p>

<h2>Чи розбудить, якщо телефон беззвучний?</h2>
<p>Так. Вібрація не залежить від бокового перемикача, а тон і так типово вимкнений.</p>

<h2>Чи посадить це батарею за ніч?</h2>
<p>Екран лишається ввімкненим усю ніч, тож так, помітно — тримайте телефон на зарядці. Це плата
за хвилю, яка справді грає.</p>

<h2>Я купив хвилі, а вони замкнені</h2>
<p>Відкрийте налаштування в застосунку й торкніться <strong>Відновити покупку</strong>, увійшовши
в той Apple ID, яким купували.</p>

<h2>Чому немає версії для iPad чи Mac?</h2>
<p>Hushwake цілком побудований навколо Taptic Engine, який є лише в iPhone. Без нього від
застосунку не лишилося б нічого. Тому — лише iPhone, свідомо.</p>

<h2>Де мої дані?</h2>
<p>На вашому телефоні й більше ніде. Див. <a href="./">політику приватності</a>.</p>
""",
}

# --------------------------------------------------------------------------- ru

PAGES["ru"] = {
    "index": """<div class="lede">
  <p><strong>У Hushwake нет ни аккаунтов, ни серверов, ни аналитики.</strong> Приложение вообще
  не делает сетевых запросов. То немногое, что оно помнит — ваши настройки и историю подъёмов, —
  хранится на вашем iPhone и никогда его не покидает.</p>
</div>

<h2>Что мы собираем</h2>
<p>Ничего. В Hushwake нет ни SDK аналитики, ни рекламы, ни отчётов о сбоях, ни слежки любого
рода. В коде нет ни одного места, которое что-либо куда-либо отправляет.</p>

<h2>Что остаётся на вашем устройстве</h2>
<ul>
  <li><strong>История подъёмов</strong> — о последних подъёмах: дата, какая волна играла, сколько
  было заведено и разбудила ли волна.</li>
  <li><strong>Настройки</strong> — сила вибрации, включён ли тон, длина волны, гашение экрана
  и последние заведённые будильник или дневной сон.</li>
  <li><strong>Состояние покупки</strong> — открыты ли остальные волны.</li>
</ul>
<p>Всё это живёт в собственном хранилище приложения и исчезает, когда вы его удаляете.</p>

<h2>Уведомления</h2>
<p>Hushwake просит разрешение на уведомления и использует его ровно для одного —
<strong>запасного будильника</strong>. Поскольку iOS выключает тактильный движок приложения, как только
оно уходит с экрана, Hushwake ставит несколько локальных уведомлений на время вашего подъёма — на случай,
если приложение закрыто и волна сыграть не сможет.</p>
<p>Эти уведомления создаются и показываются <strong>целиком на вашем iPhone</strong>. Ни
push-сервера, ни токена устройства, и ничто из этого не попадает ни к нам, ни к кому-либо ещё.
Если в этот момент приложение на экране, они подавляются и вы их не видите. Разрешение можно
не давать или отозвать позже в настройках iOS; приложение продолжит работать, просто без
подстраховки.</p>

<h2>Чего приложение не трогает</h2>
<p>Hushwake не использует ни микрофон, ни камеру, ни датчики движения, ни геопозицию, ни
контакты, ни HealthKit, ни календарь — и никогда их не запрашивает. <strong>Он не следит
за вашим сном</strong>: он не может видеть, как вы спите, и не пытается.</p>

<h2>Звук и тактильность</h2>
<p>Необязательный тон синтезируется на вашем устройстве по рецепту, записанному в коде: ничего
не записано и ничего не транслируется.</p>

<h2>Покупки</h2>
<p>Разовую покупку полностью обрабатывает Apple через App Store. Hushwake никогда не видит ваших
платёжных данных. Мы получаем только подписанный чек, который Apple выдаёт на вашем устройстве,
и используем его для одного: узнать, открыты ли остальные волны. Он проверяется на вашем iPhone
и нам не отправляется.</p>

<h2>Дети</h2>
<p>У Hushwake рейтинг 4+, он подходит любому возрасту. Ни рекламы, ни стороннего содержимого,
ни ссылок наружу, кроме этих страниц, и никаких данных ни о ком. Единственная покупка — разовая
и необязательная, через Apple и с теми родительскими ограничениями, которые вы настроили.</p>

<h2>Ваши права</h2>
<p>Поскольку персональные данные до нас не доходят, нам нечего экспортировать, исправлять или
удалять за вас. Удаление приложения убирает всё, что Hushwake сохранял.</p>

<h2>Изменения</h2>
<p>Если эта политика изменится, дата вверху страницы изменится вместе с ней. О существенных
изменениях будет сказано и в заметках к версии.</p>

<h2>Контакт</h2>
<p>Вопросы о конфиденциальности:
<a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "terms": """<div class="lede">
  <p><strong>Hushwake — это часы.</strong> Не медицинский прибор, не лечение и не трекер сна.
  Приложение не диагностирует и не лечит бессонницу, тревожность или что-либо ещё, не измеряет
  ваш сон, и мы этого не утверждаем. Если сон вас беспокоит, говорите со специалистом, а не
  с будильником.</p>
</div>

<h2>Как работает будильник — прочитайте</h2>
<p>Волна пробуждения играет <strong>только пока Hushwake открыт на экране</strong>. Это не дефект
и не то, что мы можем исправить: iOS выключает тактильный движок приложения, как только оно уходит
с экрана. Hushwake построен именно вокруг этого — он остаётся открытым как приглушённые прикроватные
часы, и ровно это позволяет ему играть настоящую, заданную приложением волну, а не типовое
жужжание.</p>
<p>Поэтому: поставьте телефон на зарядку, оставьте Hushwake открытым и положите так, чтобы
чувствовать вибрацию. Если приложение закрыто или телефон перезагрузился до времени подъёма,
вместо волны прозвучит <strong>запасное уведомление</strong> — при условии, что вы разрешили
уведомления и не выключили подстраховку.</p>
<p><strong>Попробуйте, прежде чем полагаться.</strong> Как и с любым будильником на любом
телефоне: не делайте Hushwake единственным будильником на что-то важное — самолёт, экзамен —
пока не проснулись с ним несколько раз.</p>

<h2>Использование приложения</h2>
<p>Hushwake воспроизводит вибрацию и, по желанию, тихий тон в заданное вами время. Вы можете
пользоваться им в личных, некоммерческих целях. Нельзя перепродавать его, заниматься обратной
разработкой или использовать способом, нарушающим закон там, где вы находитесь.</p>

<h2>Здоровье и безопасность</h2>
<p>Прекратите пользоваться Hushwake, если становится неприятно. Не используйте приложение за
рулём или при работе с механизмами. Если вибрация слишком сильная или слишком слабая, её можно
настроить; если одной вибрации мало, можно включить тихий тон. Держите умеренную громкость,
особенно в наушниках.</p>

<h2>Покупки</h2>
<p>Hushwake бесплатен и содержит две полноценные волны, без рекламы и без ограничений по времени.
Открыть остальные — по желанию, за <strong>один разовый платёж</strong>. Это не подписка: ничто
не продлевается и не списывается повторно.</p>
<p>Цена показывается в приложении в вашей валюте до любого подтверждения. Средства списываются
с вашего Apple ID в момент подтверждения покупки. Покупка привязана к Apple ID и восстанавливается
на других ваших устройствах с экрана покупки.</p>

<h2>Возврат средств</h2>
<p>Покупки обрабатывает Apple, поэтому и возвраты — тоже Apple, по условиям App Store, а не нами.
Запросы подаются через
<a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>

<h2>Гарантии и ответственность</h2>
<p>Hushwake предоставляется «как есть», без каких-либо гарантий, в пределах, допустимых законом.
В тех же пределах мы не отвечаем за косвенные или производные убытки от использования приложения,
включая проспанные подъёмы. Ничто здесь не ограничивает ответственность, которую закон
ограничивать не позволяет, а ваши потребительские права в вашей стране остаются в силе.</p>

<h2>Apple</h2>
<p>Apple не является стороной этих условий и не обязана оказывать поддержку Hushwake. Apple —
третье лицо-выгодоприобретатель этих условий и вправе требовать их исполнения.</p>

<h2>Изменения</h2>
<p>Эти условия могут меняться; дата вверху страницы меняется вместе с ними.</p>

<h2>Контакт</h2>
<p><a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a></p>
""",

    "support": """<div class="lede">
  <p>Что-то не работает или есть идея, как должно быть? Напишите на
  <a href="mailto:sich.io.app@gmail.com">sich.io.app@gmail.com</a>. Этот ящик читает человек,
  обычно в течение пары дней.</p>
</div>

<h2>Будильник не сработал</h2>
<p>Почти всегда это значит, что приложение не было на экране. Волна играет только пока Hushwake
открыт — iOS выключает тактильный движок приложения, как только оно уходит с экрана. Оставляйте приложение на ночном
экране, а телефон на зарядке.</p>
<p>Включите <strong>Разбудить в любом случае</strong> в настройках и разрешите уведомления, чтобы
подстраховка прозвучала, если приложение всё же закроется.</p>

<h2>Почему приложение должно оставаться открытым?</h2>
<p>Потому что именно это делает волну возможной. Закрытое приложение в лучшем случае может
попросить iOS показать уведомление, и вибрация, которую вы тогда чувствуете, принадлежит системе:
всегда одной и той же формы, всегда короткая. Оставаясь открытым, Hushwake управляет Taptic
Engine напрямую: волна начинается ниже порога ощущения, нарастает минутами и продолжается, пока
вы её не остановите.</p>

<h2>Я ничего не чувствую</h2>
<p>Проверьте, что <strong>Настройки → Звуки, тактильные сигналы → Тактильные сигналы
системы</strong> включены и телефон не в режиме энергосбережения, который ослабляет тактильность.
В приложении может быть прикручена <strong>Сила</strong>. И кладите телефон туда, где вибрация до
вас дойдёт: в мягком матрасе она теряется, на тумбочке — передаётся.</p>

<h2>Экран почти чёрный</h2>
<p>Это ночной циферблат делает своё дело: он гаснет, чтобы свет не держал вас без сна, и светлеет
вместе с волной. Если не хотите, чтобы приложение вообще трогало яркость, выключите
<strong>Гасить экран</strong> в настройках. Ваша яркость всегда возвращается при выходе
с экрана.</p>

<h2>Какую волну выбрать?</h2>
<p>Начните с <strong>Прилива</strong>. Если просыпаетесь до его конца, попробуйте
<strong>Рассвет</strong> — он дольше держится ниже порога. Если просыпаете, попробуйте
<strong>Стук</strong>. Коснитесь любой волны в списке, чтобы почувствовать её конец, прежде чем
на неё полагаться, и загляните в историю: волны, которые вы проспали не раз, отмечены.</p>

<h2>Разбудит ли, если телефон беззвучный?</h2>
<p>Да. Вибрация не зависит от бокового переключателя, а тон и так по умолчанию выключен.</p>

<h2>Не посадит ли это батарею за ночь?</h2>
<p>Экран остаётся включённым всю ночь, так что да, заметно — держите телефон на зарядке. Это плата
за волну, которая действительно играет.</p>

<h2>Я купил волны, а они закрыты</h2>
<p>Откройте настройки в приложении и нажмите <strong>Восстановить покупку</strong>, войдя в тот
Apple ID, которым покупали.</p>

<h2>Почему нет версии для iPad или Mac?</h2>
<p>Hushwake целиком построен вокруг Taptic Engine, который есть только в iPhone. Без него от
приложения ничего бы не осталось. Поэтому — только iPhone, намеренно.</p>

<h2>Где мои данные?</h2>
<p>На вашем телефоне и больше нигде. См. <a href="./">политику конфиденциальности</a>.</p>
""",
}
