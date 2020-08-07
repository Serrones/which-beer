# Which Beer?
Do you wanna choose a good beer for you?
Here you can see all details from a specif beer
or get surprised with and randomic one.
It returns a list beers by brew date, if you wish


## how to use

- build a docker image from Dockerfile `docker build -t which-beer .`

- run a container from the builded image `docker run -it --rm --name beer which-beer bash`

## commands

- main help `punk`

- beers help `punk beers`

- beer by id `punk beers beer-id <number>`

- random beer `punk beers random`

- list by brew date `punk beers brewed-before <mm-yyyy>`
