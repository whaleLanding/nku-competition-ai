document.querySelectorAll('.slot').forEach(slot => {
    let isInCooldown = false;
    
    slot.addEventListener('mouseenter', () => {
        if (!isInCooldown) {
            slot.classList.add('slot-back');
            
            // 添加冷却状态
            isInCooldown = true;
            slot.classList.add('cooldown');
            

            setTimeout(() => {
                isInCooldown = false;
                slot.classList.remove('cooldown');
            }, 500);
        }
    });
    
    slot.addEventListener('mouseleave', () => {
        slot.classList.remove('slot-back');
    });
});