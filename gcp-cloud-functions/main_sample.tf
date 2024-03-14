provider "google" {
  project = "73160070374"
  region  = "us-west1"
  zone    = "us-west1-a"
}

resource "google_compute_instance" "ollama_instance" {
  name         = "ollama-instance-1"
  machine_type = "e2-medium"
  zone         = "us-west1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
      size  = 10
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
    }
  }

  tags = ["http-server", "https-server"]

  metadata = {
    startup-script = <<EOF
#! /bin/bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common gnupg2
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install -y docker-ce
sudo systemctl start docker
sudo systemctl enable docker
docker pull ollama/ollama
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

EOF
  }
}
