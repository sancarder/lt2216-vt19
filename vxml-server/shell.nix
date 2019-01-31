{ nixpkgs ? import <nixpkgs> {} }:
let
   nixpkgs_source = fetchTarball https://github.com/NixOS/nixpkgs/archive/18.09.tar.gz;
   # Older configuration:
   # nixpkgs_source = fetchTarball https://github.com/NixOS/nixpkgs/archive/53835c93cb4bc1c6228ee04d6788398a8ab36ab4.tar.gz;
   # nixpkgs_source = /local_dir; # for local directory
   # nixpkgs_source = nixpkgs.fetchFromGitHub { # for safety of checking the hash
   #    owner = "NixOS";
   #    repo = "nixpkgs";
   #    rev = "f78e904e336156d807b2594cb6637cb070b577d7";
   #    sha256 = "0vrnk5jc1klbxlnlysnpimvyrjpvnv8y38fsx129anmc80xs8vsi";
   #  }; 
in
with (import nixpkgs_source {}).pkgs;

let py = (python36.buildEnv.override {
  extraLibs =  with python36Packages; 
    [flask
     # you can add other packages here. (comment out as necessary)
     # scikitimage
     # gensim
     # scikitlearn
    ];
  ignoreCollisions = true;});
in pkgs.stdenv.mkDerivation {
    name = "python-env";
    buildInputs = [ py ];
    shellHook = ''
      export PYTHONIOENCODING=UTF-8
      '';
     }