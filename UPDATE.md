# update steps for mpb

## commit changes

- Update version in `constants.py`
- Update `CHANGELOG`
- `git tag -l <version>` before `git push`

## manual build/deploy steps

- `make build` and `make promote` on workstation
- `make build-micro` and `make promote-micro` on k8s node
- `microk8s kubectl rollout restart -n mr-poopybutthole deploy/mr-poopybutthole` to pull new image
