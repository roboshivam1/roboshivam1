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
<td width="58%" valign="top">

### SCHOOL CONTENT ENGINE
<sub>WORKSHOP · *Teaching a machine how to make 'tasteful' school posters*</sub>

It started with one blurry annual-day photo on a school's Instagram, shot from the third row, half a curtain in frame. Every school has that page. Nobody has the time to turn eighty photos of a sports day into something that looks like anyone cared. The photos exist; the care doesn't scale.

The engine makes the care scale. Posters are written as HTML pages — real CSS, real fonts — then opened in an invisible browser, screenshotted at exactly 1080×1080, and saved as images. That's the whole trick, and it costs nothing. Anything a browser can do, the posters can do.

Around that sit dumb configs (one file per school: colours, fonts, logo, tone) and dumb templates that know nothing about any particular school. The intelligence is the glue in between — a vision worker throwing out the blurry and the too-dark, a content worker writing captions and deciding what goes on which slide, a render worker stuffing it all into HTML and shooting every size the feed needs.

Photos in one end, branded captioned carousels out the other.

<sub>**[Read the full piece →](https://shvmkpr.in/workshop/school_content/)** · FILED UNDER: JINJA2 · LLM · PYTHON</sub>

</td>
<td width="42%" valign="top">

### CLASSIFIEDS

<sub>**LOST** — One 2.5mm hex key. Last seen doing something important. No reward offered, only relief.</sub>

<sub>**PERSONAL** — First-year CSE, LNMIIT Jaipur. Answers to Shivam.</sub>

<sub>**NOTICES** — Hot Wheels catalogued, photographed, not for sale. Stop asking.</sub>

<sub>**MISCELLANY** — The filament shelf has begun sorting itself by colour. Nobody here did this.</sub>

</td>
</tr>
</table>

---

### EDITOR'S NOTE

One reporter, no fact-checker, which is how it goes to press on time. Everything above is real and unfinished in the specific way real things are. Corrections and tips: open an issue — it is the closest thing this paper has to a letters page.

<p align="center"><sub>THE BASEMENT GAZETTE · PRINTED NIGHTLY · NO REFUNDS · <a href="https://shvmkpr.in">shvmkpr.in</a></sub></p>
