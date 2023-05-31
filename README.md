# Soveren documentation

Soveren documentation describes [Soveren](https://soveren.io) for its target audience, that is DevOps, Devs, and CTOs. 
It explains what Soveren is, how it works, how to install, use, administrate, troubleshoot it, and answers various other usage-related questions.
 
## Quick start 

To start with Soveren documentation, follow the steps below.

### Prerequisites

1. Python 3.*
2. Account on [Read the Docs](https://readthedocs.org/), a paid one.
3. Brief acquaintance with [MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).
4. (also helps to check [overriding Material theme templates](https://squidfunk.github.io/mkdocs-material/customization/#extending-the-theme))
  
### Install and use

1. Install the Material theme for MkDocs:

   ```
   pip3 install mkdocs-material
   ```

   MkDocs and other required packages are installed automatically as dependencies. 
 
2. Clone the repo:

   ```
   git clone https://github.com/soverenio/docs.git
   ```

3. Create and edit doc source files:
   
   * Create new `.md` files inside the `docs` folder.  
   * Create new subfolders to group the files if needed. Apply common sense.   
   * The files content is written in [Markdown](https://www.markdownguide.org/cheat-sheet/).
            
4. Build and deploy.
    
   As the repo is integrated with the CI/CD tool and the hosting provider, the pipeline is simple:
   
   1. Push you commit to the branch of your choice.
   2. Visit [Read the Docs](https://readthedocs.org/) to check the building process if needed. 
   3. Once the process is finished, that is usually ~1 min, open the respective doc version on https://docs.soveren.io to see the result.

   *Test your artifacts locally before making a commit!*
   
5. Follow a Gitflow of your choice. 
   
   Current Gitflow:
      
   1. Develop and refactor in the `dev` branch.
   2. Ask the subject matter experts to review — content, grammar, and style. 
   3. When approved, merge the `dev` into the `v1` branch. The `v1` branch is set to the `stable` docs version — the default version you see on https://docs.soveren.io.
