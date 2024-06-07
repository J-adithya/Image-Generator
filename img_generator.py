from pathlib import Path
import torch
from accelerate import Accelerator
from diffusers import StableDiffusionPipeline
import io
from PIL import Image

class CFG:
    device = "cpu"  # Use CPU for compatibility
    seed = 42
    generator = torch.manual_seed(seed)  # Corrected to use manual_seed directly
    image_gen_steps = 35
    image_gen_model_id = "stabilityai/stable-diffusion-2"
    image_gen_size = (400, 400)
    image_gen_guidance_scale = 5

# Initialize the accelerator and model
accelerator = Accelerator()
image_gen_model = StableDiffusionPipeline.from_pretrained(
    CFG.image_gen_model_id, torch_dtype=torch.float32
)

image_gen_model = accelerator.prepare(image_gen_model)
image_gen_model = image_gen_model.to(CFG.device)

def generate_image(prompt, model):
    image = model(
        prompt,
        num_inference_steps=CFG.image_gen_steps,
        guidance_scale=CFG.image_gen_guidance_scale,
    ).images[0]

    image = image.resize(CFG.image_gen_size)
    return image

# Function to get user input and generate image
def get_user_input_and_generate_image():
    prompt = input("Enter the prompt for the image: ")
    image = generate_image(prompt, image_gen_model)
    image.show()  # Display the generated image
    # Optionally, you can save the image to a file
    # image.save("generated_image.png")

# Example usage
if __name__ == "__main__":
    get_user_input_and_generate_image()
