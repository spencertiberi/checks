import json
import os
import shlex

from check50 import *


class Scratch(Checks):

    @check()
    def valid(self):
        """project exists and is valid Scratch program"""

        # Make sure there is only one .sb2 file.
        filenames = list(filter(lambda filename: filename.endswith(".sb2"), os.listdir()))
        if len(filenames) > 1:
            raise Error("More than one .sb2 file found. Make sure there's only one!")
        elif len(filenames) == 0:
            raise Error("No .sb2 file found.")
        filename = filenames[0]

        # Ensure that unzipped .sb2 file contains .json file.
        if self.spawn("unzip {}".format(shlex.quote(filename))).exit():
            raise Error("Invalid .sb2 file.")
        self.require("project.json")

    @check("valid")
    def two_sprites(self):
        """project contains at least two sprites"""
        project = json.loads(File("project.json").read())

        # Loop over children: includes sprites and stages.
        num_sprites = sum("costumes" in child for child in project["children"])

        if num_sprites < 2:
            raise Error("Only {} sprite{} found, 2 required.".format(num_sprites,
                "" if num_sprites == 1 else "s"))

    @check("valid")
    def non_cat(self):
        """project contains a non-cat sprite"""
        project = json.loads(File("project.json").read())

        for child in project["children"]:

            # Skip over any non-sprites (e.g. backdrops).
            if "costumes" not in child:
                continue

            # Check if the sprite has the default costume.
            is_cat = any(costume["baseLayerMD5"] == "09dc888b0b7df19f70d81588ae73420e.svg"
                           for costume in child.get("costumes", []))

            # If it doesn't meow, we've found a non-cat sprite.
            if not is_cat:
                return

        # If we haven't returned, then no non-cat sprite found.
        raise Error("Requires a non-cat sprite.")

    @check("valid")
    def three_scripts(self):
        """project contains at least three scripts"""
        project = json.loads(File("project.json").read())

        # Add up scripts from each sprite or backdrop.
        num_scripts = sum(len(child.get("scripts", [])) for child in project["children"])

        if num_scripts < 3:
            raise Error("Only {} script{} found, 3 required.".format(num_scripts,
                "" if num_scripts == 1 else "s"))

    @check("valid")
    def uses_condition(self):
        """project uses at least one condition"""
        project = json.loads(File("project.json").read())

        # Search project scripts for an if or if/else block.
        if not project_contains_keywords(project, ["doIf", "doIfElse", "doUntil"]):
            raise Error("No conditions found, 1 required.")

    @check("valid")
    def uses_loop(self):
        """project uses at least one loop"""
        project = json.loads(File("project.json").read())

        # Search project scripts for a repeat, repeat until, or forever block.
        if not project_contains_keywords(project, ["doRepeat", "doUntil", "doForever"]):
            raise Error("No loops found, 1 required.")

    @check("valid")
    def uses_variable(self):
        """project uses at least one variable"""
        project = json.loads(File("project.json").read())

        # Look for global variables.
        if project.get("variables"):
            return

        # Look for local-to-sprite variables.
        if any(child.get("variables") for child in project["children"]):
            return

        # If we've reached this point, no variable found.
        raise Error("No variables found, 1 required.")

    @check("valid")
    def uses_sound(self):
        """project uses at least one sound"""
        project = json.loads(File("project.json").read())

        # Search scripts for a sound block.
        keywords = ["playSound:", "doPlaySoundAndWait", "playDrum", "noteOn:duration:elapsed:from:"]
        if not project_contains_keywords(project, keywords):
            raise Error("No sounds found, 1 required.")

def project_contains_keywords(project, keywords):
    """Returns True if project contains at least one of the keywords."""

    # Iterate over all sprites and backdrops, and the project itself.
    for child in project["children"] + [project]:

        # Perform a DFS on each script looking for keywords.
        if any(contains(script, keywords) for script in child.get("scripts", [])):
            return True

    return False

def contains(script, keywords):
    """Performs DFS on the script to determine if keyword exists."""

    # The keyword must be the first item in a list.
    if type(script) != list or not script:
        return False

    if script[0] in keywords:
        return True

    # Iterate over all children.
    return any(contains(child, keywords) for child in script)
