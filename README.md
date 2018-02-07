# Sparks

Sparks is a typeface for creating sparklines in text. It uses OpenType's *contextual alternates* feature to perform simple replacement operations on numbers. It works on both the desktop and the web where it works without Javascript, though it does require a modern-ish web browser that can make use of OpenType features in text. At the moment it is compatible with Microsoft Word (2010 and later), Apple Pages, Adobe Creative Cloud applications, Chrome 33+, Safari 6+, Firefox 4+, and Internet Explorer 10+. (See: http://stateofwebtype.com/ for a fuller listing of browser compatibility.)

There are currently three variations: **bars, dots, and dot-lines** (line charts with tiny dots at the joints between segments), each of which has five weight variants.

All three of the variants use a fixed scale of 0–100. If you're data only goes to e.g., 10, you'll need to first translate your numbers to be out of 100, otherwise you'll end up rendering an especially tiny chart.

The contextual alternates feature (`calt`) is baked into OpenType and Sparks simply leverages this feature in an unconventional way. It takes strings like `123{30,60,90}456` and outputs a sparkline. The example of `123{30,60,90}456` would have with three datapoints of 30, 60, and 90 framed by 123 and 456. Spaces after the commas will prevent the numbers from being transformed. Numbers outside of the brackets are never transformed.

See it working on our [website](http://aftertheflood.co/projects/atf-spark).




# Using Sparks

### On the web

When using the Sparks webfonts in a browser, you *should* enable the `calt` feature in your CSS, however it seems that these days `calt` is enabled by default in some browsers and you don't need to do anything to make it work other than assign the font to your text. Still, better safe than sorry. The CSS to explicitly turn on the feature looks like this (example pilfered from https://helpx.adobe.com/typekit/using/open-type-syntax.html#calt):

```
.yourClass {
  font-variant-ligatures: contextual;
  -moz-font-feature-settings: "calt";
  -webkit-font-feature-settings: "calt";
  font-feature-settings: "calt";
}
```

For more on this see the example code in the **tests** folder.

### In MS Word

If you are using MS Word you need to enable the "Use Contextual Alternates" feature for it to be able to draw the sparklines. You can do that simply by heading to "Format > Font > Advanced" and enabling it.

### In Adobe Illustrator

Turn on contextual alternates from the OpenType panel menu (Window > Type > OpenType). Here's a [screenshot](https://user-images.githubusercontent.com/771600/30393566-7ebc3a96-98b8-11e7-9b18-34cf6b1550c4.png).

### In Adobe InDesign

Sometimes contextual alternates are activated by default and sometimes they are not. We have no idea why. Use the OpenType menu to make sure they are turned on, which can be found in the options menu of the character palette (Character > Options > OpenType > Contextual Alternates). Here's a [screenshot](https://github.com/aftertheflood/sparks/documentation/indesign-contextual-alternates.png).




# How it works: the OpenType code

Inside the font files the code that powers the replacement operation for the **bar** and **dot** variations works like this:

```
feature calt {

  ignore sub zero' comma space;
  sub braceleft' zero' braceright' by chart.000;
  sub braceleft' zero' comma' by chart.000;
  sub zero' comma' by chart.000;
  sub zero' braceright' by chart.000;

} calt;

```

while the code for the **dot-line** variation is a bit more complicated, and looks sort of like this:

```
@theDots [ dot.000 dot.001 ... dot.100 ];
@linesTo000 [ line.000.000 line.001.000 ... line.100.000 ];
# 100 more those classes, one for each possible position.

feature calt {

  lookup dotsIgnore {
    ignore sub zero' comma space;
    # ... repeat for all 100 other numbers.
  } dotsIgnore;

  lookup DotsSolo {
    sub braceleft' zero' braceright' by dot.100;
    # ... repeat for all 100 other numbers.
  } dotsSolo;

  lookup dotsInitial {
    sub braceleft' zero' comma' by dot.000;
    # ... repeat for all 100 other numbers.
  } dotsInitial;

  lookup dotsMiddle {
    sub zero' comma' by dot.000;
    # ... repeat for all 100 other numbers.
  } dotsMiddle;

  lookup dotsFinal {
    sub zero' braceright' by dot.000;
    # ... repeat for all 100 other numbers.
  } dotsFinal;

  lookup linesAll {
    sub @theDots' dot.000 by @linesTo000;
    # ... repeat for all 100 other positions.
  } linesAll;

} calt;

```

In theory the **dot-line** variation could be just like the **bar** and **dot** variations with only a single round of glyph substitutions, however because the **dot-line** fonts are are plotting connections rather than single positions you would end up with *many* lines of code (almost 11k). Fine in the abstract, but it turns out that OpenType has a limit for how many lines of code can be in a single lookup table (around 3k – everything in a lookup table has to fit into 16 bits, because reasons), so compilation fails. There are definitely many ways around this, but it is a headache. The **dot-line** version sorts the problem by

- first setting up classes for both the dots and the lines
- then substituting numbers for the appropriate dot glyph (just like in the **bar** and **dot** variants, however here the sequence is a lot more important)
- and finally substituting the first of every pair of dots with the appropriate line

This works because OpenType substitution is a linear process in which each rule reads the output of the previous rule, so you can chain substitutions. (*So* many caveats to that statement, but that's a story for another day. For more information on how weird OpenType glyph substitution is check out [this amazing blogpost.](http://ansuz.sooke.bc.ca/entry/131))

---

### About us
[After the flood](http://aftertheflood.co/) is a design company based in London. We make new digital products and we believe data is the building material of the modern, 21st-century business. Using lean concepts, we collaborate with internal teams to harness their data and create products that users love. Organisations such as the NHS, Google, Nikkei and UEFA choose us to complement their domain knowledge with our experience in data products across many sectors, from equity finance to sports entertainment.

### License
Sparks has been distributed under the [SIL Open Font License](https://github.com/aftertheflood/spark/blob/master/LICENSE).
