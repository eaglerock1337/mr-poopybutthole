# contributing to mr-poopybutthole

If you feel like adding to the bot yourself, here's how to do that!

## forking and cloning mr-poopybutthole

If you're not familiar with `git`, you need to git gud. GitHub has a [good tutorial](https://guides.github.com/activities/hello-world/) on how Git works.

Create a fork of the repository on your own GitHub account. If you need instructions, use [this link](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

To clone your fork of the repo locally, you can either use the `git` command-line command, or use a GUI utility like [GitHub Desktop](https://desktop.github.com/).

## directory structure

For purposes of adding memes, here's the only two directories you need to care about:

- `mr_poopybutthole/resources` - images and videos go here
- `mr_poopybutthole/config` - all config files go here

## adding a command

Commands are the bot features that respond to specific command that starts with a `!`, such as `!ole` or `!wam`.

Commands are configured in the `commands.yaml` YAML file, and are formatted as follows, using the `!bobross` and `!butts` commands as exmaples:

```yaml
bobross:
  filename: bobross.jpg
  response: Ooh, wee! Looks like we're gonna have a happy little accident!
butts:
  filename: butts.gif
  response: Hold on to your butts! Ooh, wee!
```

Note that the indentation is required. All command names must be at the start of the line, and the properties of the command must be indented 2 spaces.

To add your own command, first insert it in the YAML file in alphabetical order.

Next, add a `response` for the command to say. Note that quotes aren't required except in certain situations.

If you have an image you'd like to add, specify the `filename` of the image the command will display. The file should be added to the `resources` directory with the exact filename as displayed. Note that all image types (`jpg`, `gif`, `png`, etc.) are accepted, as well as small videos like `mp4` files.

If you would like to post a random image instead, specify a list under the `filenames` header like follows:

```yaml
rando:
  filenames:
    - random_file1.jpg
    - random_file2.jpg
    - random_file3.jpg
  response: Ooh, wee! This command will post a random image from the above list!
```

Once done, make sure to upload all images specified under `filenames` to the `resources` directory as well.

## adding a listener

Listeners are the bot features that will autorepsond to certain strings that a Discord member says.

Listeners are configured in the `listeners.yaml` YAML file, and are formatted as follows, using the `adonis` listener as an example:

```yaml
adonis:
  filename: adonis.jpg
  matches:
  - adonis
  - superman
  response: Ooh, wee! I'm pretty sure that's something an adonis superman would do!
```

Note that the indentation is required, and must be 2 spaces. To add your own, first choose a unique name for the listener, and add it to the YAML file in alphabetical order.

Next, make a list of `matches` that you want the bot to respond to. For the above example, the `adonis` and `superman` will both match.

Next, specify a `response` for Mr. Poopybutthole to say in response. It should usually be a single sentence, and have "Ooh, wee!" before or after it.

Optionally, if you want to include an image, add the `filename` line with the name of the file. Make sure you upload the file to the `resources` directory as well!

Finally, you can also specify a list of images to be displayed randomly. To do so, add the list under `filenames` and upload all files to the `resources` directory. An example command is below:

```yaml
rando:
  filenames:
    - random1.jpg
    - random2.jpg
    - random3.jpg
  matches:
  - random
  - listener
  response: Ooh, wee! This is very random!
```

## submitting a pull request

Once you've added whatever listeners or commands you've wanted to, save the YAML files and make sure the images are present in the repo as well, and commit your changes to GitHub.

Next, you can submit a pull request from your fork using [this guide](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork).

Once you do that, I will review your changes and make sure they look good, requesting changes or approving and merging!

## becoming a contributor

If you're planning on doing this a lot, you can request to be added as a contributor to the repo. If I accept you, submitting pull requests are a lot easier and don't require your own fork:

- Clone my mr-poopybutthole repo to your system
- Create a new branch of the repo with a descriptive name. Here are a few recommendations as an example:
  - peters-new-commands
  - chris-adds-some-lulz
  - rob-new-memes
- Make the bot changes as you wish as described above
- Commit your changes to the branch
- Navigate to the repo on GitHub, and you will see a "create pull request" link on the main page
- Fill out the form and submit your pull request to me for approval!
