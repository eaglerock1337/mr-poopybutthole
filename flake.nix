with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "my-python-project";
  buildInputs = [ python38 pipenv ];
}