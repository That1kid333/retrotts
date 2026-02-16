require("dotenv").config();
const Replicate = require("replicate");
const fs = require("fs");
const https = require("https");

// Check if API token is set
if (!process.env.REPLICATE_API_TOKEN) {
  console.error("❌ Error: REPLICATE_API_TOKEN not found!");
  console.log("\n📝 Please create a .env file with:");
  console.log("   REPLICATE_API_TOKEN=your_token_here");
  console.log("\n🔑 Get your token from: https://replicate.com/account/api-tokens");
  process.exit(1);
}

// Initialize Replicate with your API token
const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});

// Function to download image from URL
async function downloadImage(url, filepath) {
  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      const fileStream = fs.createWriteStream(filepath);
      response.pipe(fileStream);
      fileStream.on("finish", () => {
        fileStream.close();
        resolve();
      });
      fileStream.on("error", reject);
    });
  });
}

async function generateLandscape() {
  console.log("🎨 Generating prehistoric cyberpunk landscape...\n");

  try {
    // Using FLUX-1.1 Pro for highest quality
    const output = await replicate.run(
      "black-forest-labs/flux-1.1-pro",
      {
        input: {
          prompt: `A breathtaking prehistoric mountain landscape at twilight with ancient pine forest silhouettes. Majestic snow-capped mountain peaks in the background, dense forest treeline in foreground. Cosmic starlit sky with purple and magenta nebula clouds. Color palette: deep purples (#2d1a4a, #5a3d7a), electric magentas (#ff00ff, #d580ff), cyan accents (#00ffff, #0dd9ff), and dark blacks. Atmospheric perspective with layered mountains fading into misty distance. Cinematic, ultra detailed, mystical atmosphere, 8k quality, wide angle landscape photography style, ethereal neon glow on mountain edges`,
          aspect_ratio: "16:9",
          output_format: "jpg",
          output_quality: 100,
          safety_tolerance: 2,
          prompt_upsampling: true
        }
      }
    );

    console.log("✅ Image generated successfully!");
    console.log("📥 Downloading image...\n");

    // Download the image
    const imagePath = "./images/cyberpunk-landscape.jpg";
    await downloadImage(output, imagePath);

    console.log(`✨ Landscape saved to: ${imagePath}`);
    console.log("\nNow updating index.html to use this background...");

  } catch (error) {
    console.error("❌ Error generating image:", error);
    console.log("\n💡 Make sure you've set REPLICATE_API_TOKEN environment variable");
    console.log("   Get your token from: https://replicate.com/account/api-tokens");
    console.log("   Then run: export REPLICATE_API_TOKEN=your_token_here");
  }
}

// Run the generation
generateLandscape();
