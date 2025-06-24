# Plot Accuracy & Loss for all models
import matplotlib.pyplot as plt
import os

def plot_all_metrics(SAVE_DIR, histories):
    plt.figure(figsize=(12,5))
    
    # Accuracy Plot
    plt.subplot(1,2,1)
    for name, history in histories.items():
        plt.plot(history['accuracy'], label=f'{name} Train Accuracy')
        plt.plot(history['val_accuracy'], label=f'{name} Validation Accuracy', linestyle='dashed')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.title('Model Accuracy Comparison')
    
    # Loss Plot
    plt.subplot(1,2,2)
    for name, history in histories.items():
        plt.plot(history['loss'], label=f'{name} Train Loss')
        plt.plot(history['val_loss'], label=f'{name} Validation Loss', linestyle='dashed')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Model Loss Comparison')
    
    plt.savefig(os.path.join(SAVE_DIR, "models_accuracy_loss_plot.png"))
    plt.show()