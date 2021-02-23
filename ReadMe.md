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


## DATA TO ADD
- Gamboa new paper https://osf.io/s96rw/

---

## Table of Contents
- [Installation](#installation)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

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

Pull Requests are welcome. No particular code style is enforced, however we ask that you use tabs especially when working on Python code. This helps prevent errors from inconsistent indentation.

---

## Team

| **Zane Jobe**</a> | **Jessy Liao**</a> | **Eric Klatzco**</a> | **Vlad Muresan**</a> | **Lucas Kitaev**</a> | **Bryanna Gaede**</a> |
| :---: |:---:| :---:| :---:| :---:| :---:|
| [![Zane Jobe](https://avatars0.githubusercontent.com/u/37050801?s=200)](https://github.com/zanejobe)    | [![Jessy Liao](https://avatars0.githubusercontent.com/u/31642595?s=200)](https://github.com/jetthyliao) | [![Eric Klatzco](https://avatars3.githubusercontent.com/u/24947614?s=200)](https://github.com/ericklatzco)  | [![Vlad Muresan](https://avatars1.githubusercontent.com/u/54830371?s=200)](https://github.com/imstrobey)  | [![Lucas Kitaev](https://avatars3.githubusercontent.com/u/10089400?s=200)](https://github.com/bobsmith947)  | [![Bryanna Gaede](https://avatars3.githubusercontent.com/u/60149368?s=200)](https://github.com/BryannaGaede)  |
| <a href="https://github.com/zanejobe" target="_blank">`github.com/zanejobe`</a> | <a href="https://github.com/jetthyliao" target="_blank">`github.com/jetthyliao`</a> | <a href="https://github.com/ericklatzco" target="_blank">`github.com/ericklatzco`</a> | <a href="https://github.com/imstrobey" target="_blank">`github.com/imstrobey`</a> | <a href="https://github.com/bobsmith947" target="_blank">`github.com/bobsmith947`</a> | <a href="https://github.com/BryannaGaede" target="_blank">`github.com/BryannaGaede`</a> |

---

## FAQ

- **How do I use the admin site?**
	- After making a superuser account and starting the development server, you can navigate to `http://localhost:8000/admin/` and log in. Once logged in, you will see the option to moderate `meta_table`. On the moderation page, you are given several options. Selecting a specific time period will include only uploads that were added during that time. It is also possible to filter by verified and unverified uploads. Using the checkboxes on the left enables the administrator to perform mass verification/unverification and deletion of rows.

---

## Support

Please open an issue if you are in need of support.

---

## License

This project is licensed under the Apache License 2.0.
