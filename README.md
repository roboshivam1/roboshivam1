<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/masthead-dark.svg">
  <img alt="The Basement Gazette — GitHub Edition" src="assets/masthead-light.svg" width="100%">
</picture>

<table>
<tr>
<td width="26%" valign="top">

**COLUMN ONE**

### The last version? (Apparently not)

<sub>*JAIPUR* — I have now written JARVIS three times. Each rewrite began with the belief that I finally understood what I was building, and each ended as proof that I had only understood the previous version.</sub>

<sub>MK3 starts from zero. Always-on core, intermittent workers, a durable queue that survives me closing the laptop mid-job. Five subagents doing work their namesakes would not recognise.</sub>

<sub>Phase 5 adds a notification policy and a `/quiet` command, because an assistant that never shuts up is just a smoke alarm with opinions.</sub>

</td>
<td width="46%" valign="top">

**LEAD STORY · SOFTWARE**

# CHALKDUST TEACHES ITSELF TO DRAW

<sub>*A pipeline that turns a script into a narrated animation, and the one architectural bet holding it together*</sub>

<sub>**BY SHIVAM** · STAFF ENGINEER, NIGHT EDITOR, ONLY EMPLOYEE</sub>

The scrappy version worked exactly well enough to expose the problem: a model writing Manim code freehand produces animations that overlap, overflow and wander off-frame. The rebuild inverts it. The model no longer authors animation code — it **selects and parameterizes hand-written, layout-safe components** through a JSON spec that gets validated before anything renders.

Audio is generated first, so every duration in the timeline derives from measured speech rather than a guess. Content-addressed caching, parallel beat rendering, draft and final quality tiers, a bounded repair loop, and a human gate before publish.

Three verticals: science explainers, CS fundamentals, JEE Advanced solutions.

</td>
<td width="28%" valign="top">

**INSIDE TODAY**

| | |
|:---|---:|
| Workshop | 6 |
| Motoring | 3 |
| Lab Notes | 4 |
| Classifieds | 5 |
| Op-Ed | 1 |

**THE CRITIC RECOMMENDS**

<sub>THE WORKSHOP PLAYLIST</sub>

**Rubberband Man**
<sub>THE SPINNERS · 1977</sub>

<sub>Peter Quill music is the best music.</sub>

<sub>*More at [shvmkpr.in](https://shvmkpr.in) →*</sub>

</td>
</tr>
</table>

---

<table>
<tr>
<td width="50%" valign="top">

### PATENT FILED ON AIR PURIFIER
<sub>WORKSHOP</sub>

**SqOnion** — wall-mounted, 540×540mm chassis, central fan hub, four filter tracks a side, ESP32 sensor stack. Provisional application on file with the Indian Patent Office. Prototyping moved off hand-cut MDF the day a printer entered the building, which tells you everything about hand-cut MDF.

</td>
<td width="50%" valign="top">

### MOTORCYCLE GETS REMOVABLE FACE
<sub>MOTORING</sub>

One salvaged Pulsar NS200 frame, several interchangeable printed body sets — scrambler, café racer, sports. Scrambler first. Bodywork and ESP32 auxiliaries now; motor and battery when the budget recovers. Build logs run in the print edition.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### SCHOOL RUNS ON CUSTOM SOFTWARE
<sub>LAB NOTES</sub>

Advising **Malviya Convent School** on a modular platform — FastAPI, Postgres, Redis, a box they own. One hard rule: modules talk to the core over REST and an event bus, never straight into the database. The unabridged version of this idea is called Vidyut.

</td>
<td width="50%" valign="top">

### CLASSIFIEDS

<sub>**WANTED** — First hackathon. Never been to one. Bringing a soldering iron regardless.</sub>

<sub>**FOR SALE** — Desk objects for people whose desks are also workbenches. *The Basement Supply Co*, opening shortly.</sub>

<sub>**PERSONAL** — First-year CSE, LNMIIT Jaipur. Answers to Shivam.</sub>

<sub>**NOTICES** — Hot Wheels catalogued, photographed, not for sale.</sub>

</td>
</tr>
</table>

---

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=roboshivam1&show_icons=true&hide_title=true&hide_border=true&bg_color=1b1c1e&text_color=e7e1cb&icon_color=d6786e">
    <img src="https://github-readme-stats.vercel.app/api?username=roboshivam1&show_icons=true&hide_title=true&hide_border=true&bg_color=d8d4ca&text_color=16161a&icon_color=9d262f" alt="Circulation figures">
  </picture>
</p>

---

### EDITOR'S NOTE

One reporter, no fact-checker, which is how it goes to press on time. Everything above is real and unfinished in the specific way real things are. Corrections and tips: open an issue — it is the closest thing this paper has to a letters page.

<p align="center"><sub>THE BASEMENT GAZETTE · PRINTED NIGHTLY · NO REFUNDS · <a href="https://shvmkpr.in">shvmkpr.in</a></sub></p>
