if [ ! -z $ZSH_NAME ] ; then
  MANIP_PATH="$( cd "$( dirname "$0" )" && pwd )"
elif [ ! -z $BASH ] ; then
  MANIP_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
else
  echo "Linter: Unsupported shell! Only bash and zsh supported at the moment!"
fi
export MANIP_PATH

export PATH="$PATH:$MANIP_PATH/bin"
