
# op_ace6_kbuild

Oneplus ACE6 kernel builder, can integrate KernelSU or its various and SUSFS 

## Overview

This repository provides a GitHub Actions-based automated build script suite for compiling the OnePlus ACE6 kernel, with built-in support for integrating KernelSU or ots various and SUSFS features.

It includes GitHub Actions workflow files and prebuilt auxiliary tools, without any OEM kernel source code — the kernel source code must be obtained separately from official OEM channels.

The prebuilt tool `scripts/configure` acts as a build-time helper:

- Only when specific features (KPN) are enabled, it automatically modifies  arch/arm64/Makefile  and applies patches, ensuring the final kernel image has the target features integrated as expected.
- It includes strict whitelist and blacklist verification logic: whitelisted users get unrestricted access to all features, while blacklisted users will have the entire build process directly blocked.

## Usage

1. Fork this repository

2. Enable the action

3. Trigger the GitHub Actions workflow named Build custom,and select what you want

4. Drink something, wait for building done.

5. Download the Anykernel3 package ,then flash it. Reboot to enjoy.

## License

|Component|License|Detail|
|-|-|-|
|GitHub Actions Workflows|MIT License| See the LICENSE file for details |
|Prebuilt Binary (`scripts/configure`) |BSD 2-Clause License |See the LICENSE-scripts-configure file for details |
OEM Kernel Source Code |GPLv2 License| Comply with the original terms of the OEM kernel |

## Important Notes

1. `scripts/configure` is an independent build-time auxiliary tool. It only modifies the kernel build configuration files when specific features are enabled during the build phase, does not participate in kernel compilation or linking, and is not embedded into the final kernel image.

2. The modification behavior of `scripts/configure` does not affect the GPLv2 licensing of the OEM kernel source code.

3. When redistributing this repository, the original copyright notice and license text must be retained. When redistributing the compiled kernel package, users only need to comply with the GPLv2 terms of the OEM kernel and do not need to include the license information of this repository.

4. The maintainer reserves the right of access control via the whitelist/blacklist logic in `scripts/configure`, which does not violate the terms of the BSD 2-Clause License.

 