# Design Ideas

This file is dedicated to software design ideas for the `honda` package manager.
It is organized along specific design issues one must deal with when writing
a package manager. While going over these issues, I will do my best to first describe
how [conda][conda] works and deals with these issues. At the same time, I will
highlight what works well, and propose my suggested changes.

## Installation

The [conda][conda] package manager is currently available for installation via shell
and EXE scripts. This practice allows for several benefits:

- Good support for Windows
- Terms of Service (TOS) is distributed and presented this way
- Installs custom version of Python (is this true?)

This process is in line with how other package managers in the Python world work
(see: [poetry][poetry] and [pdm][pdm]) and should continue to work this way as
it can guarantee that `honda` is installed into an isolated environment.

With that being said, what `conda` cannot currently is being installed purely via
`pip` (poetry can)

## Configuration

The configuration for the application comes from a variety of sources in this order:

1. Config file parameters marked with `#!final`, `#!top`, or `#!bottom`
2. Environment variables `CONDA_*`
3. CLI parameters
4. Config file specified with `CONDARC`
5. System and user config files (parsed in order)

After collect the configuration from these locations, they will have to be merged
accordingly according to the above rules. Additional things to watch out for:

- dict -> merged
- list -> merged
- str -> clobbered (higher precedence wins out)

At the end of this process, we should have a single object in our application where
the configuration can be retrieved.


## Operating system support (Win/OSX/*nix)

[conda]: https://github.com/conda/conda

[pdm]: https://pdm.fming.dev/

[poetry]: https://python-poetry.org/
