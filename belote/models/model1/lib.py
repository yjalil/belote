import tensorflow as tf
from dataclasses import dataclass


@dataclass
class Params :
    BATCH_SIZE : int = 32
    INPUT_HEIGHT : int = 120
    INPUT_WIDTH : int = 100
    CLASSES : int = 32
    EPOCHS : int = 200

def initialize_model() :
    model = tf.keras.models.Sequential([
            tf.keras.layers.Resizing(Params.INPUT_HEIGHT,Params.INPUT_WIDTH),
            tf.keras.layers.Conv2D(64, (2, 2), activation="relu", padding="same"),
            tf.keras.layers.MaxPooling2D((2, 2)),

            tf.keras.layers.Conv2D(128, (2, 2), activation="relu", padding="same"),
            tf.keras.layers.MaxPooling2D((2, 2)),

            tf.keras.layers.Conv2D(256, (2, 2), activation="relu", padding="same"),
            tf.keras.layers.MaxPooling2D((2, 2)),

            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),

            tf.keras.layers.Dense(Params.CLASSES, activation='softmax')
        ])
    print("✅ Model initialized")

    return model


def compile_model(model) :
    model.compile('adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    print("✅ Model compiled")

    return model

def train_model(
        model,
        train_ds,
        val_ds,
        epochs=Params.EPOCHS,
        batch_size = Params.BATCH_SIZE,
        callbacks = [tf.keras.callbacks.EarlyStopping(patience = 5,
                                                      monitor="val_loss",
                                                      restore_best_weights=True,
                                                      verbose = 2)]):


    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
    )

    print(f"✅ Model trained ")

    return model, history
