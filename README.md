# Soveren documentation

Soveren documentation describes [Soveren](https://soveren.io) for its target audience, that is DevOps, Devs, and CTOs. 
It explains what Soveren is, how it works, how to install, use, administrate, troubleshoot it, and answers various other usage-related questions.
 
## Quick start 

To start with Soveren, follow these steps.

### Prerequisites

1. Python 3.*
2. Account on [Read the Docs](https://readthedocs.org/), a paid one.
3. Brief acquaintance with [MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).
  
### Install and use

1. Install the Material theme for MkDocs:

   ```
   pip install mkdocs-material
   ``` 
   or   
   ```
   python3 pip -m mkdocs-material
   ```

   MkDocs and other required packages are installed automatically as dependencies. 
 
2. Clone the repo:

   ```
   git clone https://github.com/soverenio/docs.git
   ```

3. Learn the structure:

   ``` sh
   .
   ├─ customize/                          # Customized templates to override the Material theme templates
   ├─ docs/
   │  ├─ administration/                  # Group of doc pages related to Soveren administration
   │  ├─ dashboards/                      # Group of doc pages related Soveren cloud dashboards
   │  ├─ getting-started/                 # Group of doc pages related getting started with Soveren
   │  ├─ img/                             # Images, logos, favicons
   │  ├─ js/                              # Custom JS scripts applied on each doc page
   │  ├─ miscellaneous/                   # Doc pages not fitting any specific group
   │  ├─ stylesheets/                     # Custom stylesheets that either add new styles or override some theme styles.
   │  ├─ troubleshooting/                 # Group of doc pages related troubleshooting Soveren
   │  ├─ index.html                       # Main doc page
   │  └─ requirements.txt                 # Dependencies to install when building the project via a CI/CD tool
   ├─ .readthedocs.yaml                   # Read the Docs configuration file — the CI/CD tool
   ├─ mkdocs.yml                          # MkDocs configuration file
   └─ README.md                           # Project readme
   ```

   Also, check:
   * [Soveren cloud dashboards](https://app.soveren.io)
   * [Overriding Material theme templates](https://squidfunk.github.io/mkdocs-material/customization/#extending-the-theme)

4. Create and edit doc source files:
   
   * Create new `.md` files inside the `docs` folder.  
   * Create new subfolders to group the files if needed. Apply common sense.   
   * The files content is written in [Markdown](https://www.markdownguide.org/cheat-sheet/).
            
5. Build and deploy.
    
   As the repo is integrated with the CI/CD tool and the hosting provider, the pipeline is simple:
   
   1. Push you commit to the branch of your choice.
   2. Visit [Read the Docs](https://readthedocs.org/) to check the building process if needed. 
   3. Once the process is finished, that is usually ~1 min, open the respective doc version on https://docs.soveren.io to see the result.

   *Test your artifacts locally before making a commit!*
   
6. Follow a Gitflow of your choice. 
   
   Current Gitflow:
      
   1. Develop and refactor in the `dev` branch.
   2. Ask the subject matter experts to review — content, grammar, and style. 
   3. When approved, merge the `dev` into the `v1` branch. The `v1` branch is set to the `stable` docs version — the default version you see on https://docs.soveren.io.
   
   
   



  
   
