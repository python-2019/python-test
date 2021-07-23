REM "start.....".
SET /p dir="input git root path"
CD %dir%
REM "into %dir%"
PAUSE

SET develop=develop
SET master=master
SET /p release="input you release branch: "

SET /p op="F:finish release,S:start release:"
REM "you op is %op%"

git checkout %master%
git branch -vv
git pull

git checkout %develop%
git branch -vv
git pull

IF %op%==F (
git checkout %release%
git branch -vv
git pull
mvn jgitflow:release-finish -DallowSnapshots=true -Dmaven.test.skip=true -Dmaven.javadoc.skip=true
)
IF %op%==S (
mvn jgitflow:release-start -DallowSnapshots=true -DautoVersionSubmodules=true -Dmaven.test.skip=true
)
REM "finish....."
PAUSE