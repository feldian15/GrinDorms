#!/bin/bash

# Handle arguments
case "$1" in
  deploy)
    echo "Deploy option selected. (Not implemented yet.)"
    ;;

  demo)
    echo "Launching demo..."
    bash "~/ROOT/Demos/GrinDormsDemo/launch.bash"
    ;;

  logs)
    echo "Showing logs..."
    journalctl -u django.service
    ;;

  *)
    echo "Usage: $0 {deploy|demo|logs}"
    exit 1
    ;;
esac
