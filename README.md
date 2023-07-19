# ComponentFileScrubber

## Intro
Have you built a ServiceNow UI Builder Component and tried sharing it with a co-worker, industry contact, or the ServiceNow community? If so whoever it was shared with likely encountered an error when trying to develop with and deploy the component as the file-paths will be associated with the incorrect app-creator company code!


To remedy this issue you could find and replace every instance of your company creator code, your component name, and then validate (hoping you didn't miss anything). This is fine if it's a one off issue but when we created our [UI Builder Component Template](https://github.com/esolutionsone/component-template) we also built the file scrubber to expedite this process! 
 
---

- [Intro](#intro)
- [How to use this Component](#how-to-use-this-component)

---

## How to use this component
1) Clone the [UI Builder Component Template](https://github.com/esolutionsone/component-template) from git
2) Run npm install
3) Run "npm run rename"
4) Follow the steps in the wizard to rename the app creator company code & component name if necessary!

**There are two versions of the renamer in this repo (python and node) >> the node.js version is what's included in our template!**

**This scrubber has a try at your own risk policy!**