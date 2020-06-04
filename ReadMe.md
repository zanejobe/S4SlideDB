<img src="https://offtheshelfedge.files.wordpress.com/2015/02/submarine-landslide-japan-yamamoto-1.jpg?w=300" title="Underwater Landslide" alt="An outcrop of an ancient underwater landslide"></a>

<img src="https://sites.google.com/a/utexas.edu/s4slide/_/rsrc/1427127385050/config/customLogo.gif?revision=10" ></a>

# S4SlideDB : Underwater Landslides Database

> To create a new interactive website for the storage, visualization, and analysis of underwater landslide dimensions (also known as subaqueous landslides, mass transport deposits, slumps, slides, debris flows)

## Wireframe slide deck
https://docs.google.com/presentation/d/1hrxL_wvtDWWL8yOhDuUMt4J_Qua39owmmJgzqqn-J-E/edit?usp=sharing

## Pertinent links
- Clare et al paper https://sp.lyellcollection.org/content/477/1/455.abstract
- 2020 Slides meeting https://www.slidesdublin2020.com
- S4Slide webpage https://sites.google.com/a/utexas.edu/s4slide/
- This project sponsored by ESIP https://www.esipfed.org

## Team

| **Zane Jobe**</a> | **Jessy Liao**</a> | **Eric Klatzco**</a> | **Vlad Muresan**</a> | **Lucas Kitaev**</a> | **Bryanna Gaede**</a> |
| :---: |:---:| :---:| :---:| :---:| :---:|
| [![Zane Jobe](https://avatars0.githubusercontent.com/u/37050801?s=200)](https://github.com/zanejobe)    | [![Jessy Liao](https://avatars0.githubusercontent.com/u/31642595?s=200)](https://github.com/jetthyliao) | [![Eric Klatzco](https://avatars3.githubusercontent.com/u/24947614?s=200)](https://github.com/ericklatzco)  | [![Vlad Muresan](https://avatars1.githubusercontent.com/u/54830371?s=200)](https://github.com/imstrobey)  | [![Lucas Kitaev](https://avatars3.githubusercontent.com/u/10089400?s=200)](https://github.com/bobsmith947)  | [![Bryanna Gaede](https://avatars3.githubusercontent.com/u/60149368?s=200)](https://github.com/BryannaGaede)  |
| <a href="https://github.com/zanejobe" target="_blank">`github.com/zanejobe`</a> | <a href="https://github.com/jetthyliao" target="_blank">`github.com/jetthyliao`</a> | <a href="https://github.com/ericklatzco" target="_blank">`github.com/ericklatzco`</a> | <a href="https://github.com/imstrobey" target="_blank">`github.com/imstrobey`</a> | <a href="https://github.com/bobsmith947" target="_blank">`github.com/bobsmith947`</a> | <a href="https://github.com/BryannaGaede" target="_blank">`github.com/BryannaGaede`</a> |

- You can just grab their GitHub profile image URL
- You should probably resize their picture using `?s=200` at the end of the image URL.

---
# Other stuff for later... (copied this ReadMe template from fvcproductions)

**Badges will go here**

- build status


[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Dependency Status](http://img.shields.io/gemnasium/badges/badgerbadgerbadger.svg?style=flat-square)](https://gemnasium.com/badges/badgerbadgerbadger) [![Coverage Status](http://img.shields.io/coveralls/badges/badgerbadgerbadger.svg?style=flat-square)](https://coveralls.io/r/badges/badgerbadgerbadger) [![Code Climate](http://img.shields.io/codeclimate/github/badges/badgerbadgerbadger.svg?style=flat-square)](https://codeclimate.com/github/badges/badgerbadgerbadger) [![Github Issues](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/issues.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger/issues) [![Pending Pull-Requests](http://githubbadges.herokuapp.com/badges/badgerbadgerbadger/pulls.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger/pulls) [![Gem Version](http://img.shields.io/gem/v/badgerbadgerbadger.svg?style=flat-square)](https://rubygems.org/gems/badgerbadgerbadger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) [![Badges](http://img.shields.io/:badges-9/9-ff6799.svg?style=flat-square)](https://github.com/badges/badgerbadgerbadger)

- For more on these wonderful ~~badgers~~ badges, refer to <a href="http://badges.github.io/badgerbadgerbadger/" target="_blank">`badgerbadgerbadger`</a>.


- Most people will glance at your `README`, *maybe* star it, and leave
- Ergo, people should understand instantly what your project is about based on your repo

> Tips

- HAVE WHITE SPACE
- MAKE IT PRETTY
- GIFS ARE REALLY COOL

> GIF Tools

- Use <a href="http://recordit.co/" target="_blank">**Recordit**</a> to create quicks screencasts of your desktop and export them as `GIF`s.
- For terminal sessions, there's <a href="https://github.com/chjj/ttystudio" target="_blank">**ttystudio**</a> which also supports exporting `GIF`s.

**Recordit**

![Recordit GIF](http://g.recordit.co/iLN6A0vSD8.gif)

**ttystudio**

![ttystudio GIF](https://raw.githubusercontent.com/chjj/ttystudio/master/img/example.gif)

---

## Table of Contents (Optional)

> If your `README` has a lot of info, section headers might be nice.

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

---

## Example (Optional)

```javascript
// code away!

let generateProject = project => {
  let code = [];
  for (let js = 0; js < project.length; js++) {
    code.push(js);
  }
};
```

---

## Installation

[Django 3.0.x](https://www.djangoproject.com/download/), [Node.js 10+](https://nodejs.org/en/download/), and [sqlite3](https://www.sqlite.org/download.html) are required for this project.

### Clone

```
$ git clone https://github.com/zanejobe/S4SlideDB.git
$ cd S4SlideDB
```

### Setup

> install npm dependencies

`$ npm install`

> import sample data

```
$ cd s4slide
$ sqlite3 -init import.sql db.sqlite3
```

> run the development server

`$ npm start`

> compile `main.ts`

```
$ npm run type-check
$ npm run build
```

> create an account on the admin site

`$ python3 s4slide/manage.py createsuperuser`

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/joanaz/HireDot2.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/joanaz/HireDot2/compare/" target="_blank">`https://github.com/joanaz/HireDot2/compare/`</a>.

---

## FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="http://fvcproductions.com" target="_blank">`fvcproductions.com`</a>
- Twitter at <a href="http://twitter.com/fvcproductions" target="_blank">`@fvcproductions`</a>
- Insert more social links here.

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2015 © <a href="http://fvcproductions.com" target="_blank">FVCproductions</a>.
