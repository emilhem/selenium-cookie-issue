{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    nativeBuildInputs = with pkgs.buildPackages; [
      python311
      chromedriver
      geckodriver
      firefox
      chromium
      (python311.withPackages(ps: with ps; [
          virtualenv
          pytest
          selenium
      ]))
    ];
  }