import gradio as gr
import warnings
from diffusers import StableDiffusionPipeline
from accelerate import Accelerator

# Suppress specific deprecation warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="diffusers.models.transformers.transformer_2d")

def generate_image(prompt):
    accelerator = Accelerator()
    # Initialize the Stable Diffusion model
    image_gen_model = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2").to(accelerator.device)

    # Generate image using the provided prompt
    generated_images = image_gen_model(prompt, num_inference_steps=35, guidance_scale=5).images

    if len(generated_images) > 0:
        # Return the first generated image (PIL image)
        return generated_images[0]
    else:
        # Handle case where no images are generated
        raise ValueError("No images generated.")

iface = gr.Interface(fn=generate_image, 
                     inputs="text", 
                     outputs="image",
                     title="Text-to-Image Generator using Stable Diffusion",
                     description="Generate images from text prompts using Stable Diffusion.")
iface.launch(server_port=7860)
