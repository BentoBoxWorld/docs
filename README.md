# 🍱 BentoBox Documentation

Welcome to the official source repository for the BentoBox documentation. This repository contains all the raw documentation files (in reStructuredText/Markdown) that are used to build the official documentation website.

-----

## 📖 Read The Docs

The live, published documentation is viewable at:

**[https://docs.bentobox.world](https://docs.bentobox.world)**

> If you are just looking to read the documentation or find help with BentoBox, please visit the link above. This repository is for **contributing** to the documentation.

-----

## 🤝 Contributing

We welcome and appreciate all contributions, from fixing a simple typo to writing an entire new guide for an addon. Your help makes BentoBox better for everyone.

### How It Works

1.  **Fork** this repository to your own GitHub account.
2.  **Create a new branch** for your changes (e.g., `fix/update-config-guide` or `feat/new-limits-addon-doc`).
3.  **Make your edits** to the files.
4.  **Commit and push** your changes to your fork.
5.  **Open a Pull Request (PR)** from your branch to the `main` branch of this repository.

-----

## 🚀 Automated Build Process

This repository is directly connected to the **[ReadTheDocs](https://readthedocs.org/)** service, which handles the build and deployment pipeline.

  * **On Commit/Merge:** When new commits are pushed to the `main` branch (usually from a merged Pull Request), a webhook is sent to ReadTheDocs.
  * **Build:** ReadTheDocs pulls the latest changes from this repository and runs its build process to compile the raw files into a static HTML website.
  * **Publish:** If the build is successful, the new version of the documentation is automatically published and made live.

Your contribution will appear on **[https://docs.bentobox.world](https://docs.bentobox.world)** within a few minutes of your Pull Request being merged.

## 📄 License

The text and content of the BentoBox documentation (this repository) are licensed under the **[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)**.

Code snippets included within the documentation are, unless otherwise noted, licensed under the **[MIT License](https://opensource.org/licenses/MIT)**.